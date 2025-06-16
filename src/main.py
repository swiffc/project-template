"""Main entry point for the cursor development system."""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .core.core_types import ExecutionContext, ProjectType
from .modules.file_organizer import FileOrganizerModule
from .modules.project_creator import ProjectCreatorModule

app = FastAPI(title="Unified Web Application")

# Mount the frontend static files
app.mount("/static", StaticFiles(directory="dist"), name="static")


# API routes
@app.get("/api/health")  # type: ignore[misc]
async def health_check() -> dict:
    """Return health status of the API."""
    return {"status": "healthy"}


# Serve the frontend for all other routes
@app.get("/{path:path}")  # type: ignore[misc]
async def serve_frontend(path: str, request: Request) -> FileResponse:
    """Serve the frontend application."""
    # If the path starts with /api, let FastAPI handle it
    if path.startswith("api"):
        return None

    # Serve the frontend index.html for all other routes
    return FileResponse("dist/index.html")


def setup_logging() -> None:
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Cursor Development System - Project Scaffolding Tool"
    )

    parser.add_argument("project_name", help="Name of the project to create")

    parser.add_argument(
        "--type",
        "-t",
        type=str,
        choices=[t.value for t in ProjectType],
        required=True,
        help="Type of project to create",
    )

    parser.add_argument(
        "--output", "-o", type=str, help="Output directory path (default: ./projects)"
    )

    parser.add_argument(
        "--advanced",
        "-a",
        action="store_true",
        help="Enable advanced mode with additional features",
    )

    parser.add_argument(
        "--github", "-g", action="store_true", help="Enable GitHub integration"
    )

    parser.add_argument(
        "--skip-install", "-s", action="store_true", help="Skip dependency installation"
    )

    parser.add_argument(
        "--template", type=str, default="default", help="Template variant to use"
    )

    parser.add_argument("--config", type=str, help="Path to custom configuration file")

    return parser.parse_args()


def create_project(args: argparse.Namespace) -> Optional[Path]:
    """Create a new project and return the project root path if successful."""
    try:
        # Create execution context
        context = ExecutionContext(
            project_name=args.project_name,
            project_type=ProjectType(args.type),
            output_path=Path(args.output) if args.output else None,
            advanced_mode=args.advanced,
            github_integration=args.github,
            skip_install=args.skip_install,
            template_variant=args.template,
            config_override=Path(args.config) if args.config else None,
        )

        # Initialize modules
        project_creator = ProjectCreatorModule()
        file_organizer = FileOrganizerModule()

        # Execute project creation
        if not project_creator.validate(context):
            logging.error("Project creation validation failed")
            return None

        result = project_creator.execute(context)
        if not result.success:
            logging.error(f"Project creation failed: {result.message}")
            return None

        # Execute file organization
        if not file_organizer.validate(context):
            logging.error("File organization validation failed")
            return None

        result = file_organizer.execute(context)
        if not result.success:
            logging.error(f"File organization failed: {result.message}")
            return None

        return context.project_root

    except Exception as e:
        logging.error(f"Project creation failed: {str(e)}")
        return None


def main() -> None:
    """Run the main application entry point."""
    try:
        # Set up logging
        setup_logging()

        # Parse arguments
        args = parse_args()

        # Create project
        project_root = create_project(args)
        if not project_root:
            return

        logging.info(f"Project created successfully at: {project_root}")

    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
