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
----------------------------------------------------
### 🛠️ Installation & Usage

## ✅ Step 1: Setup Your Environment
### 🔧 1.1 Install Python
Make sure Python 3.8 or higher is installed. You can check with:
```bash
python --version
```
### 📦 1.2 Install Poetry (for dependency & script management)
Poetry handles packages and sets up projects cleanly.
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Then confirm it works:
```bash
poetry --version
```

## 📁 Step 2: Create a New Project
In your terminal:
```bash
poetry new pubmed-affiliation-checker
cd pubmed-affiliation-checker
```
Now your folder will look like:
```
pubmed-affiliation-checker/
├── pyproject.toml
├── pubmed_affiliation_checker/
└── tests/
```
## 📦 Step 3: Add Dependencies
Update your pyproject.toml under [tool.poetry.dependencies]:
```
[tool.poetry.dependencies]
python = "^3.10"
biopython = "^1.81"
click = "^8.1.3"
pandas = "^2.0.0"
requests = "^2.31"
python-dotenv = "^1.0.0"
```
Then install everything:
```bash
poetry install
```
## 🧠 Step 4: Get a Groq API Key
```
Go to https://console.groq.com
Sign up / sign in → Go to API Keys
Generate a key and copy it
Then create a .env file at the root level:
```
env
```

GROQ_API_KEY=your_key_here
```
## 📁 Step 5: Create the CLI Script
Create a file called cli.py inside src/pubmed_affiliation_checker:

## 🌐 Step 6: Fetch Data from PubMed
Create fetch.py inside src/pubmed_affiliation_checker:


## 🔗 Step 7: Integrate Groq LLM 
Create llm.py inside src/pubmed_affiliation_checker:

## 🚀 Step 8: Run Your Program!
Add to pyproject.toml:
```toml
[tool.poetry.scripts]
get-papers-list = "pubmed_affiliation_checker.cli:main"
```
Then activate the shell:
```
	poetry env info --path
    path\to\your\venv\Scripts\activate
```
**Without shell activation you can also run the CLI command**
## Final O/P :- Run the CLI
* Example 1 :- file called result.csv will be created in root directory 
```
	get-papers-list "covid drug" -f result.csv -d
```
* Example 2:-Without shell activation 
```
	poetry run get-papers-list "cancer immunotherapy" -f results.csv -d

```
--------------------------------------------------------------
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

###  🧱 Development Steps Followed
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

### 🔧 Tools and Libraries Used
# 🌐 Groq LLM API
Used for affiliation classification using models like llama-3.3-70b-versatile. → Groq Developer Console → Groq Docs

# 🧬 Biopython
For interacting with PubMed’s Entrez API and processing MEDLINE data. → Biopython Website

# 📦 Poetry
Dependency management and CLI packaging. → Poetry Documentation

# 🐼 Pandas
For structured output and CSV export. → Pandas Docs

# 🖱️ Click
For building the CLI interface and handling user input. → Click Docs



## 🌍 Author
Made with ❤️ by Shreenidhi 