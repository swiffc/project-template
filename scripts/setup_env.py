#!/usr/bin/env python3
"""Environment setup script for Cursor Development System."""

import sys
from pathlib import Path
from typing import Dict

from src.core.env_manager import EnvManager

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))


def setup_environment() -> None:
    """Set up environment configuration."""
    print("Setting up environment configuration...")

    # Initialize environment manager
    env_manager = EnvManager()

    # Get the source .env file path
    source_env = Path("C:/Users/Dcornealius/Documents/GitHub/project-template/.env")
    if not source_env.exists():
        print(f"Error: Source .env file not found at {source_env}")
        return

    # Read the source .env file
    env_vars: Dict[str, str] = {}
    with open(source_env, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

    # Save to global environment
    env_manager.save_global_env(env_vars)
    print(f"Environment configuration saved to {env_manager.env_file}")

    # Copy to current project if it exists
    current_project = Path.cwd()
    if (current_project / "src").exists():
        env_manager.copy_to_project(current_project)
        print("Environment configuration copied to current project")

    print("\nEnvironment setup complete!")
    print("\nYour environment variables are now available in:")
    print(f"1. Global config: {env_manager.env_file}")
    print("2. Current project (if applicable)")
    print("\nTo use these variables in your code:")
    print("from src.core.env_manager import EnvManager")
    print("env_manager = EnvManager()")
    print("env_manager.load_global_env()")
    print("value = env_manager.get_env_value('YOUR_VARIABLE')")


if __name__ == "__main__":
    setup_environment()
