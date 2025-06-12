"""Script to run deep research analysis on a given topic."""

from dotenv import load_dotenv

from src.ai.research import deep_research


def main() -> None:
    """Run the deep research analysis."""
    load_dotenv()
    prompt = (
        "The Cursor Development System is a modern, open-source project scaffolding tool for Python, JavaScript, and "
        "full-stack projects. It features strict typing, pre-configured templates, automated validation, deep AI "
        "integration, and a complexity-based development workflow. How does it compare to other popular project "
        "templates or scaffolding tools like Create React App, Yeoman, Cookiecutter, or Nx? What are its strengths and "
        "weaknesses for professional developers?"
    )
    results = deep_research(prompt)
    print("\nResearch Results:")
    print("=" * 50)
    for key, value in results.items():
        print(f"\n{key}:")
        print("-" * 30)
        print(value)


if __name__ == "__main__":
    main()
