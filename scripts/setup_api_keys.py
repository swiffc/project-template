#!/usr/bin/env python3
"""
Script to securely set up API keys for the project.

This script will:
1. Create a .env file if it doesn't exist
2. Prompt for API keys
3. Securely store them in the .env file
"""

import getpass
import os
from pathlib import Path
from typing import Dict, Optional

from dotenv import load_dotenv


def get_env_path() -> Path:
    """Get the path to the .env file."""
    return Path.home() / ".env"


def load_existing_keys() -> Dict[str, str]:
    """Load existing API keys from .env file."""
    env_path = get_env_path()
    if not env_path.exists():
        return {}

    load_dotenv(env_path)
    return {
        "PERPLEXITY_API_KEY": os.getenv("PERPLEXITY_API_KEY", ""),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY", ""),
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY", ""),
        "MISTRAL_API_KEY": os.getenv("MISTRAL_API_KEY", ""),
    }


def save_keys(keys: Dict[str, str]) -> None:
    """Save API keys to .env file."""
    env_path = get_env_path()

    # Create .env file if it doesn't exist
    if not env_path.exists():
        env_path.touch()

    # Update or add new keys
    new_lines = []
    for key, value in keys.items():
        if value:  # Only add non-empty values
            new_lines.append(f"{key}={value}")

    # Write back to file
    env_path.write_text("\n".join(new_lines) + "\n")
    print(f"\nAPI keys have been saved to {env_path}")


def get_api_key(service: str, existing: Optional[str] = None) -> str:
    """Prompt for an API key."""
    if existing:
        print(f"\nExisting {service} API key found.")
        if input("Would you like to update it? (y/N): ").lower() != "y":
            return existing

    return getpass.getpass(f"Enter your {service} API key: ")


def main() -> None:
    """Set up API keys for the project."""
    print("Setting up API keys for your project...")

    # Load existing keys
    existing_keys = load_existing_keys()

    # Get new keys
    keys = {
        "PERPLEXITY_API_KEY": get_api_key(
            "Perplexity", existing_keys.get("PERPLEXITY_API_KEY")
        ),
        "OPENAI_API_KEY": get_api_key("OpenAI", existing_keys.get("OPENAI_API_KEY")),
        "ANTHROPIC_API_KEY": get_api_key(
            "Anthropic", existing_keys.get("ANTHROPIC_API_KEY")
        ),
        "GROQ_API_KEY": get_api_key("Groq", existing_keys.get("GROQ_API_KEY")),
        "MISTRAL_API_KEY": get_api_key("Mistral", existing_keys.get("MISTRAL_API_KEY")),
    }

    # Save keys
    save_keys(keys)
    print("\nAPI keys have been set up successfully!")


if __name__ == "__main__":
    main()
