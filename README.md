# Cursor Development System

A powerful, modern project scaffolding tool that helps developers create and manage projects with best practices, strict typing, modular architecture, and deep AI integration.

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Creating a New Project](#creating-a-new-project)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Environment Variables & Secrets](#environment-variables--secrets)
- [Deep Research (AI Integration)](#deep-research-ai-integration)
- [Customizing Templates](#customizing-templates)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features
- 🏗️ **Production-Ready Templates** for React, Next.js, FastAPI, Electron, Python, and more
- 🔒 **Strict Typing** (TypeScript, Python type hints)
- 🧩 **Modular, Universal Folder Structure**
- 🤖 **Deep AI Integration** (Anthropic, Perplexity, Google)
- 🛠️ **Automated Validation, Linting, and Testing**
- 🧠 **Complexity-Based, Phased Development Workflow**
- 🔐 **Secure Secrets Management** with `.env` and pre-commit hooks
- 📚 **Automated Documentation and Code Quality Enforcement**

---

## Prerequisites
- Python 3.10+
- Node.js 18+ (for JS/TS projects)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [git](https://git-scm.com/)
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/)

---

## Installation

Clone the repository and install dependencies:

```bash
# Clone the repo
git clone https://github.com/swiffc/project-template.git
cd project-template

# Set up Python virtual environment (recommended)
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# (Optional) Install Node.js dependencies for JS/TS templates
# cd into your generated project and run:
npm install
```

---

## Creating a New Project

Use the built-in script to scaffold a new project:

```bash
python scripts/dev.py setup

# Or use the batch file (Windows):
./create-project.bat [project-type] [project-name] [options]

# Example:
./create-project.bat react-spa my-awesome-app --github
```

**Supported project types:**
- react-spa, nextjs-fullstack, vue-nuxt, express-api, fastapi-backend, electron-desktop, python-automation, windows-automation, cad-automation, ai-ml-project, static-website

**Options:**
- `--github` : Enable GitHub integration
- `--advanced` : Enable advanced mode
- `--template [variant]` : Use a specific template variant
- `--output [path]` : Set output directory

---

## Project Structure

```text
project-root/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration
├── .cursor/       # AI configuration
├── scripts/       # Automation scripts
├── assets/        # Static assets
├── data/          # Data files
├── output/        # Generated files
├── tools/         # Development tools
├── examples/      # Usage examples
```

---

## Development Workflow

**Set up the development environment:**
```bash
python scripts/dev.py setup
```

**Run tests:**
```bash
python scripts/dev.py test
```

**Run linting and type checks:**
```bash
python scripts/dev.py lint
```

**Validate project structure:**
```bash
python scripts/validate.py
```

**Run all checks:**
```bash
python scripts/dev.py all
```

---

## Environment Variables & Secrets

1. **Create a `.env` file in your project root:**
   ```env
   ANTHROPIC_API_KEY=your_anthropic_key
   PERPLEXITY_API_KEY=your_perplexity_key
   GOOGLE_API_KEY=your_google_key
   # Add any other secrets or config here
   ```
2. **Never commit your `.env` file!** It is already in `.gitignore`.
3. **Share `.env.example` (if needed) with placeholders for team members.**

---

## Deep Research (AI Integration)

The system includes a research module for advanced research using Anthropic, Perplexity, and Google APIs.

**Setup:**
- Add your API keys to `.env` as above.
- Install dependencies:
  ```bash
  pip install requests python-dotenv
  ```

**Run deep research:**
1. Edit `run_deep_research.py` to set your prompt (see examples below).
2. Run:
   ```bash
   python run_deep_research.py
   ```

**Example prompt:**
```python
prompt = (
    "The Cursor Development System is a modern, open-source project scaffolding tool for Python, JavaScript, and full-stack projects. "
    "It features strict typing, pre-configured templates, automated validation, deep AI integration, and a complexity-based development workflow. "
    "How does it compare to other popular project templates or scaffolding tools like Create React App, Yeoman, Cookiecutter, or Nx? "
    "What are its strengths and weaknesses for professional developers?"
)
```

**Sample code:**
```python
from dotenv import load_dotenv
load_dotenv()
from src.ai.research import deep_research
results = deep_research(prompt)
for provider, result in results.items():
    print(f"{provider}:\n{result}\n")
```

---

## Customizing Templates
- Edit files in `src/modules/` to add or modify project templates.
- Update `.cursor/rules/` for custom AI rules and project standards.
- Add new scripts to `scripts/` for automation.
- Update `pyproject.toml` and `requirements.txt` for Python dependencies.
- Update `package.json` for JS/TS dependencies.

---

## Troubleshooting
- **API key errors:** Double-check your `.env` file and that the correct APIs are enabled for your keys.
- **Google API 403:** Ensure the Generative Language API is enabled and billing is set up.
- **Perplexity 404:** You may need to request access to the Perplexity API.
- **Anthropic cautious answers:** Provide more context in your prompt.
- **Pre-commit hook failures:** Run `python scripts/dev.py lint` and fix any reported issues.
- **Missing dependencies:** Run `pip install -r requirements.txt` and `pip install python-dotenv requests`.

---

## Contributing
Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [Cursor AI](https://cursor.sh) for the amazing development environment
- All contributors who have helped shape this project
