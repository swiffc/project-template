"""Project Creator Module."""

import json
from datetime import datetime

from ..core.core_types import ExecutionContext, ModuleResult, ProjectType
from ..core.module import BaseModule


class ProjectCreatorModule(BaseModule):
    """Module for creating new projects."""

    def __init__(self) -> None:
        """Initialize ProjectCreatorModule."""
        super().__init__("project_creator", "Creates project directory structure")

    def execute(self, context: ExecutionContext) -> ModuleResult:
        """Execute project creation."""
        try:
            self.log_info(f"Creating project: {context.project_name}")

            # Create project root directory
            context.project_root.mkdir(parents=True, exist_ok=True)

            # Create base directory structure
            self._create_base_structure(context)

            # Create project metadata
            self._create_project_metadata(context)

            # Create base files
            self._create_base_files(context)

            return ModuleResult(
                module_name=self.name,
                success=True,
                message=(f"Project structure created at: " f"{context.project_root}"),
                data={"project_root": str(context.project_root)},
            )

        except Exception as e:
            self.log_error(f"Project creation failed: {e}")
            return ModuleResult(
                module_name=self.name, success=False, message=str(e), error=e
            )

    def _create_base_structure(self, context: ExecutionContext) -> None:
        """Create base directory structure."""
        base_dirs = [
            "src",
            "tests",
            "docs",
            "config",
            ".cursor",
            ".cursor/rules",
            ".cursor/scripts",
        ]

        for dir_name in base_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            self.log_info(f"Created directory: {dir_path}")

        # Create project-type specific structure
        self._create_type_specific_structure(context)

    def _create_type_specific_structure(self, context: ExecutionContext) -> None:
        """Create project-type specific directories."""
        type_structures = {
            ProjectType.REACT_SPA: [
                "src/components",
                "src/pages",
                "src/hooks",
                "src/utils",
                "src/styles",
                "public",
                "public/assets",
            ],
            ProjectType.FASTAPI_BACKEND: [
                "src/api",
                "src/core",
                "src/models",
                "src/services",
                "src/utils",
                "database",
                "migrations",
                "tests/unit",
                "tests/integration",
            ],
            ProjectType.PYTHON_AUTOMATION: [
                "src/automation",
                "src/workflows",
                "src/tasks",
                "src/utils",
                "data/input",
                "data/output",
                "data/temp",
                "logs",
            ],
            ProjectType.WINDOWS_AUTOMATION: [
                "src/scripts",
                "src/modules",
                "src/utils",
                "config/environments",
                "logs/execution",
                "logs/errors",
                "outputs/reports",
            ],
        }

        dirs = type_structures.get(context.project_type, [])
        for dir_name in dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_project_metadata(self, context: ExecutionContext) -> None:
        """Create project metadata file."""
        metadata = {
            "project": {
                "name": context.project_name,
                "type": context.project_type.value,
                "created": datetime.now().isoformat(),
                "creator": "Cursor Development System",
                "version": "1.0.0",
                "execution_id": context.execution_id,
            },
            "structure": {
                "src": "Source code directory",
                "tests": "Test files and test data",
                "docs": "Project documentation",
                "config": "Configuration files",
                ".cursor": "Cursor AI configuration",
            },
            "development": {
                "complexity_based": True,
                "phases": ["architecture", "api", "ui", "polish"],
                "validation_enabled": True,
                "consistency_checks": True,
            },
            "features": {
                "advanced_mode": context.advanced_mode,
                "github_integration": context.github_integration,
                "template_variant": context.template_variant,
            },
        }

        metadata_file = context.project_root / ".cursor" / "project.json"
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        self.log_info("Project metadata created")

    def _create_base_files(self, context: ExecutionContext) -> None:
        """Create base project files."""
        # Create .gitignore
        self._create_gitignore(context)

        # Create README.md
        self._create_readme(context)

        # Create basic .cursorrules
        self._create_cursorrules(context)

    def _create_gitignore(self, context: ExecutionContext) -> None:
        """Create comprehensive .gitignore file."""
        gitignore_content = """# Dependencies
node_modules/
__pycache__/
*.pyc
.env
.env.local
.venv
venv/

# Build outputs
dist/
build/
*.egg-info/
.next/
out/

# IDE
.vscode/
.idea/
*.swp
*.swo
.vs/

# OS
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Cache
.cache/
.pytest_cache/
.coverage
htmlcov/

# Temporary files
*.tmp
*.temp
.temp/

# Cursor specific
.cursor/temp/
*.cursor-tmp

# Environment files (keep templates)
.env
.env.local
.env.*.local
!.env.example
!.env.development
!.env.staging
!.env.production
"""

        gitignore_file = context.project_root / ".gitignore"
        with open(gitignore_file, "w", encoding="utf-8") as f:
            f.write(gitignore_content)

    def _create_readme(self, context: ExecutionContext) -> None:
        """Create comprehensive README.md."""
        readme_content = f"""# {context.project_name}

**Project Type:** {context.project_type.value}
**Created:** {datetime.now().strftime('%Y-%m-%d')}
**Generated by:** Cursor Development System v2.0.0

## 🏗️ Project Structure

This project follows **complexity-based development** principles:

### Development Phases:
1. **Architecture Phase** - Core systems and database design
2. **API Phase** - Backend services and data layer
3. **UI Phase** - User interface and components
4. **Polish Phase** - Optimization and deployment

## 🚀 Quick Start

```bash
cd {context.project_name}
# Follow the phase-based development approach
# Start with the most complex components first
```

## 📁 Directory Structure

```
{context.project_name}/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration
└── .cursor/       # AI configuration
```

## 🤖 Cursor AI Integration

This project is optimized for Cursor AI with:
- Smart .cursorrules for context-aware assistance
- Modular architecture following best practices
- Automated validation and consistency checking
- Phase-based development workflow

## 📚 Documentation

- See `docs/` for detailed documentation
- Check `.cursor/project.json` for project metadata
- Review `.cursorrules` for AI configuration

## 🔧 Available Scripts

Run the development environment:
```bash
python scripts/dev.py
```

Validate project structure:
```bash
python scripts/validate.py
```

## 🎯 Development Workflow

This project uses complexity-based development. Start with:
1. Core architecture and database design
2. API endpoints and business logic
3. User interface components
4. Styling and optimization
"""

        readme_file = context.project_root / "README.md"
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(readme_content)

    def _create_cursorrules(self, context: ExecutionContext) -> None:
        """Create basic .cursorrules file."""
        cursorrules_content = f"""# {context.project_name} - Cursor AI Rules
# Generated by Cursor Development System v2.0.0
# Project Type: {context.project_type.value}

## PROJECT OVERVIEW
- **Name**: {context.project_name}
- **Type**: {context.project_type.value}
- **Architecture**: Modular with Separation of Concerns
- **Development**: Complexity-based phased approach

## DEVELOPMENT PHASES (Follow this order)

### Phase 1: Architecture (Highest Complexity)
- Database schema and core models
- Authentication and security systems
- Core business logic and algorithms
- System architecture decisions

### Phase 2: API Layer (High Complexity)
- REST/GraphQL API endpoints
- Data validation and serialization
- Error handling and middleware
- Service layer implementation

### Phase 3: UI Layer (Medium Complexity)
- User interface components
- Forms and user interactions
- Navigation and routing
- State management

### Phase 4: Polish (Low Complexity)
- Styling and visual design
- Performance optimization
- Testing and documentation
- Deployment configuration

## CODING STANDARDS

### Universal Rules:
- Always use @codebase for cross-file changes
- Maintain consistency across all files
- Follow naming conventions strictly
- Implement comprehensive error handling
- Write self-documenting code

### File Organization:
- Group related functionality together
- Use clear, descriptive file names
- Maintain consistent directory structure
- Keep modules focused and cohesive

### Quality Gates:
- No print/console.log statements in production
- No hardcoded credentials or secrets
- All functions must have error handling
- Follow project-specific naming conventions

## VALIDATION RULES

Before saving any file:
1. Check syntax and structure
2. Verify naming conventions
3. Ensure error handling exists
4. Validate against project standards

## CONSISTENCY ENFORCEMENT

- Use @codebase when updating interfaces
- Apply changes to ALL related files
- Maintain uniform patterns across codebase
- Update documentation with code changes

This configuration ensures AI-assisted development follows
best practices and maintains high code quality.
"""

        cursorrules_file = context.project_root / ".cursorrules"
        with open(cursorrules_file, "w", encoding="utf-8") as f:
            f.write(cursorrules_content)
