# tests/test_affiliation_checker.py

from pubmed_affiliation_checker.llm import is_pharma_affiliation

def test_known_company_affiliation():
    aff = "Pfizer Inc., Groton, CT"
    assert is_pharma_affiliation(aff) is True

def test_known_academic_affiliation():
    aff = "Department of Chemistry, Indian Institute of Science"
    assert is_pharma_affiliation(aff) is False
