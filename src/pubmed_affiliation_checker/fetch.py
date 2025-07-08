from Bio import Entrez
import pandas as pd
import re
from typing import List
from .llm import is_pharma_affiliation

Entrez.email = "shreenidhi1903@gmail.com"

def fetch_and_filter(query: str, debug: bool = False) -> pd.DataFrame:
    """
    Fetches PubMed papers matching the search query and filters those with authors
    affiliated to pharmaceutical or biotech companies using an LLM.

    Args:
        query (str): PubMed search term.
        debug (bool): If True, prints debug information from LLM and API responses.

    Returns:
        pd.DataFrame: A DataFrame of filtered papers with non-academic authors.
    """
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=15)
        record = Entrez.read(handle)
        ids: List[str] = record.get("IdList", [])
    except Exception as e:
        if debug:
            print(f"❌ PubMed search error: {e}")
        return pd.DataFrame()

    results = []

    for pmid in ids:
        try:
            handle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
            text = handle.read()
        except Exception as e:
            if debug:
                print(f"⚠️ Failed to fetch PubMed ID {pmid}: {e}")
            continue

        title_match = re.search(r"TI\s+-\s+(.*)", text)
        authors = re.findall(r"FAU\s+-\s+(.*)", text)
        affiliations = re.findall(r"AD\s+-\s+(.*)", text)
        pub_date = re.search(r"DP\s+-\s+(\d{4})", text)
        email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+", text)

        non_acad_authors: List[str] = []
        company_affiliations: List[str] = []

        for author, aff in zip(authors, affiliations):
            try:
                if is_pharma_affiliation(aff, debug=debug):
                    non_acad_authors.append(author)
                    company_affiliations.append(aff)
            except Exception as llm_error:
                if debug:
                    print(f"⚠️ LLM error while processing affiliation: {llm_error}")
                continue

        if non_acad_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title_match.group(1).strip() if title_match else "N/A",
                "Publication Date": pub_date.group(1) if pub_date else "N/A",
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": email_match.group(0) if email_match else "N/A"
            })

    return pd.DataFrame(results)