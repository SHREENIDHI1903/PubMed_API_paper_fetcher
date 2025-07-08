# PubMed Affiliation Checker

A Python command-line tool to search PubMed and identify papers with authors affiliated to pharmaceutical, biotech, or commercial health organizations using Groq's LLM.

## 🔧 Usage

```bash
get-papers-list "cancer immunotherapy" -f output.csv -d
```

## Options
* -f / --file: Save output to CSV

* -d / --debug: Enable LLM debug logs

* -h / --help: Show CLI help

### ✅ Output Columns
* PubmedID

* Title

* Publication Date

* Non-academic Author(s)

* Company Affiliation(s)

* Corresponding Author Email

### 💡 Powered by
* PubMed via BioPython

* Groq LLMs

* Python, Click, Poetry