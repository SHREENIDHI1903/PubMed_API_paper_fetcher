# PubMed Affiliation Checker

A Python command-line tool to search PubMed and identify papers with authors affiliated to pharmaceutical, biotech, or commercial health organizations using Groq's LLM.

---

## 🚀 Features

- 🔍 Search PubMed for papers using a free-text query
- 🧬 Use Groq's high-speed LLM (LLaMA 3 or Mistral replacements) to detect non-academic affiliations
- 📄 Output structured results to CSV (or print to console)
- 🛠️ Fully modular, typed, and Poetry-managed Python project
- ⚙️ CLI options for file saving, debugging, and help

---

## 🔧 Usage

```bash
get-papers-list "cancer immunotherapy" -f output.csv -d
```

## Options
* -f / --file: Save output to CSV

* -d / --debug: Enable LLM debug logs

* -h / --help: Show CLI help

## ✅ Output Columns

PubmedID

Title

Publication Date

Non-academic Author(s)

Company Affiliation(s)

Corresponding Author Email

## 💡 Powered by
* PubMed via BioPython

* Groq LLMs

* Python, Click, Poetry

## 🧱 Development Steps Followed
## 📁 Phase 1: Project Bootstrapping
* Created structured Poetry project with --src layout

* Defined pyproject.toml with required dependencies

* Organized code into cli.py, fetch.py, and llm.py for clear separation of concerns

## 🧪 Phase 2: PubMed Search Integration
* Used Entrez from Biopython to search and fetch papers

* Parsed MEDLINE format using regex to extract:

* Title

* Authors

* Affiliations

* Publication Date

* Corresponding Email

## 🧠 Phase 3: LLM-Based Affiliation Classification
* Integrated with Groq API

* Updated model to llama-3.3-70b-versatile after mixtral deprecation

* Constructed prompts to request binary classification ("Yes"/"No" + reason)

## 🧑‍💻 Phase 4: CLI Design and UX
* Built CLI with click supporting:

		* --file: Save to CSV

		* --debug: Show detailed logs

		* --help: Display usage

* Added type hints, comments, and docstrings

## 🔐 Phase 5: Secret Handling and Git Cleanup
* Used .env to store API keys securely

* Added .env to .gitignore

* Rotated and revoked leaked keys detected by GitHub

* Ensured safe Git history via git rm --cached .env


## 💡 Technologies Used
* Python 3.10+

* Biopython (PubMed access)

* Click (CLI interface)

* Pandas (CSV output)

* Requests (HTTP calls to Groq)

* Groq API (LLM-based classification)

* Poetry (environment + dependency manager)

## 🌍 Author
Made with ❤️ by Shreenidhi 