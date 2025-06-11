"""File organizer module for the cursor development system."""

import json

from ..core.core_types import ExecutionContext, ModuleResult, ProjectType
from ..core.module import BaseModule


class FileOrganizerModule(BaseModule):
    """Organizes file layouts and creates configuration files."""

    def __init__(self) -> None:
        """Initialize FileOrganizerModule."""
        super().__init__("file_organizer", "Organizes files and creates configurations")

    def validate(self, context: ExecutionContext) -> bool:
        """Validate file organizer can execute."""
        if not super().validate(context):
            return False

        if not context.project_root.exists():
            self.log_error(f"Project directory does not exist: {context.project_root}")
            return False

        return True

    def execute(self, context: ExecutionContext) -> ModuleResult:
        """Execute file organization."""
        try:
            self.log_info(f"Organizing files for {context.project_type.value}")

            # Create universal project structure
            self._create_universal_structure(context)

            # Create type-specific structure
            self._create_type_specific_structure(context)

            # Create configuration files
            self._create_configuration_files(context)

            # Create environment files
            self._create_environment_files(context)

            # Create development tools
            self._create_development_tools(context)

            return ModuleResult(
                module_name=self.name,
                success=True,
                message="File organization completed successfully",
            )

        except Exception as e:
            self.log_error(f"File organization failed: {e}")
            return ModuleResult(
                module_name=self.name, success=False, message=str(e), error=e
            )

    def _create_universal_structure(self, context: ExecutionContext) -> None:
        """Create universal project structure."""
        universal_dirs = [
            ".cursor",  # Cursor settings
            ".github",  # CI/CD workflows
            "docs",  # Documentation
            "src",  # Source code
            "scripts",  # Automation scripts
            "config",  # Configuration files
            "tests",  # Test files
            "assets",  # Static assets
            "data",  # Data files
            "output",  # Generated files
            "tools",  # Development tools
            "examples",  # Usage examples
        ]

        for dir_name in universal_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            self.log_info(f"Created directory: {dir_path}")

    def _create_type_specific_structure(self, context: ExecutionContext) -> None:
        """Create project-type specific structure."""
        if context.project_type == ProjectType.REACT_SPA:
            self._create_web_structure(context)
        elif context.project_type == ProjectType.FASTAPI_BACKEND:
            self._create_backend_structure(context)
        elif context.project_type == ProjectType.WINDOWS_AUTOMATION:
            self._create_windows_structure(context)
        elif context.project_type == ProjectType.CAD_AUTOMATION:
            self._create_cad_structure(context)
        elif context.project_type == ProjectType.ELECTRON_DESKTOP:
            self._create_desktop_structure(context)

    def _create_web_structure(self, context: ExecutionContext) -> None:
        """Create web application structure."""
        web_dirs = [
            "src/components/common",
            "src/components/forms",
            "src/components/layout",
            "src/components/ui",
            "src/pages",
            "src/hooks",
            "src/services",
            "src/store",
            "src/utils",
            "src/types",
            "src/constants",
            "src/styles",
        ]

        for dir_name in web_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_backend_structure(self, context: ExecutionContext) -> None:
        """Create backend/API structure."""
        backend_dirs = [
            "src/controllers",
            "src/models",
            "src/services",
            "src/middleware",
            "src/routes",
            "src/database/migrations",
            "src/database/seeds",
            "src/database/queries",
            "src/utils",
            "src/validators",
            "src/types",
            "src/config",
        ]

        for dir_name in backend_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_windows_structure(self, context: ExecutionContext) -> None:
        """Create Windows automation structure."""
        windows_dirs = [
            "src/automation/windows",
            "src/automation/file-operations",
            "src/automation/registry",
            "src/automation/services",
            "src/automation/ui-automation",
            "src/modules",
            "src/configs",
            "src/templates",
            "src/logs",
            "src/utils",
            "data/input",
            "data/output",
            "data/templates",
            "data/backups",
        ]

        for dir_name in windows_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_cad_structure(self, context: ExecutionContext) -> None:
        """Create CAD automation structure."""
        cad_dirs = [
            "src/cad-scripts/autocad",
            "src/cad-scripts/solidworks",
            "src/cad-scripts/fusion360",
            "src/cad-scripts/inventor",
            "src/drawing-tools",
            "src/parametric",
            "src/export-import",
            "src/assemblies",
            "src/libraries",
            "src/templates",
            "assets/cad-templates",
            "assets/materials",
            "assets/standards",
            "assets/symbols",
            "data/drawings",
            "data/models",
            "data/exports",
            "data/specifications",
        ]

        for dir_name in cad_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_desktop_structure(self, context: ExecutionContext) -> None:
        """Create desktop application structure."""
        desktop_dirs = [
            "src/main",
            "src/renderer",
            "src/windows",
            "src/dialogs",
            "src/services",
            "src/ipc",
            "src/database",
            "src/utils",
            "src/assets",
            "resources/icons",
            "resources/images",
            "resources/fonts",
            "resources/sounds",
        ]

        for dir_name in desktop_dirs:
            dir_path = context.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_configuration_files(self, context: ExecutionContext) -> None:
        """Create project configuration files."""
        # Create .cursorrules with organization standards
        cursorrules_content = f"""# {context.project_name} - Cursor AI Rules
# Generated by Cursor Development System v2.0.0
# Project Type: {context.project_type.value}

## UNIVERSAL PROJECT STRUCTURE
Adapt this structure based on project type. Always maintain consistent organization principles.

```
project-root/
├── .cursor/                    # Cursor settings
├── .github/                    # CI/CD workflows
├── docs/                       # Documentation
├── src/                        # Source code (main development)
├── scripts/                    # Automation and build scripts
├── config/                     # Configuration files
├── tests/                      # Test files
├── assets/                     # Static assets
├── data/                       # Data files and databases
├── output/                     # Generated/compiled files
├── tools/                      # Development tools and utilities
└── examples/                   # Usage examples
```

## FILE TYPE ORGANIZATION RULES

### COMPONENTS AND UI ELEMENTS
**Location:** `src/components/` or `src/ui/`
**Naming:** PascalCase (Button.tsx, UserProfile.jsx, MainWindow.cs)
**Structure:**
```
ComponentName/
├── index.ts                   # Export file
├── ComponentName.tsx          # Main component
├── ComponentName.module.css   # Styles
├── ComponentName.test.tsx     # Tests
└── ComponentName.types.ts     # Types
```

### AUTOMATION SCRIPTS
**Location:** `src/automation/` or `scripts/`
**Naming:** kebab-case or camelCase depending on language
- PowerShell: `Get-SystemInfo.ps1`
- Python: `system_monitor.py`
- Batch: `backup-files.bat`
- VBScript: `AutoCAD_BatchProcess.vbs`

### API AND SERVICE FILES
**Location:** `src/services/` or `src/api/`
**Naming:** camelCase with Service suffix
- `userService.ts`
- `authenticationService.py`
- `windowsRegistryService.cs`

### UTILITY FUNCTIONS
**Location:** `src/utils/` or `src/helpers/`
**Naming:** camelCase describing purpose
- `dateUtils.ts`
- `fileOperations.py`
- `cadGeometry.js`
- `registryHelper.ps1`

### CONFIGURATION FILES
**Location:** `config/` or `src/config/`
**Naming:** Purpose-based naming
- `database.config.js`
- `api.settings.json`
- `automation.config.xml`
- `cad.standards.json`

## LANGUAGE-SPECIFIC RULES

### TYPESCRIPT/JAVASCRIPT
- Components: PascalCase (.tsx, .jsx)
- Utilities: camelCase (.ts, .js)
- Types: camelCase with .types.ts suffix
- Constants: SCREAMING_SNAKE_CASE or camelCase

### PYTHON
- Modules: snake_case (.py)
- Classes: PascalCase
- Functions: snake_case
- Constants: SCREAMING_SNAKE_CASE

### C#/.NET
- Classes: PascalCase (.cs)
- Interfaces: IPascalCase
- Methods: PascalCase
- Private fields: _camelCase

### POWERSHELL
- Scripts: Verb-Noun.ps1 (Get-SystemInfo.ps1)
- Functions: Verb-Noun format
- Variables: $camelCase

## IMPORT AND REFERENCE RULES

### ABSOLUTE IMPORTS (Use for):
- Cross-feature references
- Core utilities and services
- Shared components
- Configuration files

### RELATIVE IMPORTS (Use for):
- Files in same directory
- Parent/child relationships
- Feature-specific modules

### IMPORT ORDER:
1. External libraries/frameworks
2. Internal absolute imports
3. Relative imports (parent directories)
4. Relative imports (same directory)
5. Type imports (TypeScript)

## QUALITY STANDARDS

### Every file should have:
1. **Clear purpose** - Single responsibility
2. **Proper location** - Following organizational rules
3. **Consistent naming** - Following language conventions
4. **Appropriate imports** - Clean dependency management
5. **Documentation** - Comments explaining purpose

### Before creating any file:
1. Check if similar functionality exists
2. Determine the correct location using these rules
3. Use appropriate naming convention
4. Set up proper imports/exports
5. Add basic documentation
"""

        cursorrules_file = context.project_root / ".cursorrules"
        with open(cursorrules_file, "w", encoding="utf-8") as f:
            f.write(cursorrules_content)

        # Create type-specific configuration files
        if context.project_type == ProjectType.REACT_SPA:
            self._create_react_configs(context)
        elif context.project_type == ProjectType.FASTAPI_BACKEND:
            self._create_fastapi_configs(context)
        elif context.project_type == ProjectType.PYTHON_AUTOMATION:
            self._create_python_configs(context)

    def _create_react_configs(self, context: ExecutionContext) -> None:
        """Create React configuration files."""
        # package.json
        package_json = {
            "name": context.project_name.lower().replace(" ", "-"),
            "version": "1.0.0",
            "type": "module",
            "description": "Generated by Cursor Development System",
            "scripts": {
                "dev": "vite",
                "build": "tsc && vite build",
                "preview": "vite preview",
                "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
                "lint:fix": "eslint . --ext ts,tsx --fix",
                "format": 'prettier --write "src/**/*.{ts,tsx,json,css,md}"',
                "type-check": "tsc --noEmit",
                "test": "vitest",
                "test:coverage": "vitest --coverage",
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-router-dom": "^6.8.0",
            },
            "devDependencies": {
                "@types/react": "^18.2.0",
                "@types/react-dom": "^18.2.0",
                "@typescript-eslint/eslint-plugin": "^6.0.0",
                "@typescript-eslint/parser": "^6.0.0",
                "@vitejs/plugin-react": "^4.0.0",
                "eslint": "^8.45.0",
                "eslint-plugin-react-hooks": "^4.6.0",
                "eslint-plugin-react-refresh": "^0.4.3",
                "prettier": "^3.0.0",
                "typescript": "^5.0.2",
                "vite": "^4.4.5",
                "vitest": "^0.34.0",
            },
        }

        package_file = context.project_root / "package.json"
        with open(package_file, "w", encoding="utf-8") as f:
            json.dump(package_json, f, indent=2)

        # tsconfig.json
        tsconfig = {
            "compilerOptions": {
                "target": "ES2020",
                "useDefineForClassFields": True,
                "lib": ["ES2020", "DOM", "DOM.Iterable"],
                "module": "ESNext",
                "skipLibCheck": True,
                "moduleResolution": "bundler",
                "allowImportingTsExtensions": True,
                "resolveJsonModule": True,
                "isolatedModules": True,
                "noEmit": True,
                "jsx": "react-jsx",
                "strict": True,
                "noUnusedLocals": True,
                "noUnusedParameters": True,
                "noFallthroughCasesInSwitch": True,
                "baseUrl": ".",
                "paths": {
                    "@/*": ["src/*"],
                    "@/components/*": ["src/components/*"],
                    "@/hooks/*": ["src/hooks/*"],
                    "@/utils/*": ["src/utils/*"],
                },
            },
            "include": ["src"],
            "references": [{"path": "./tsconfig.node.json"}],
        }

        tsconfig_file = context.project_root / "tsconfig.json"
        with open(tsconfig_file, "w", encoding="utf-8") as f:
            json.dump(tsconfig, f, indent=2)

    def _create_fastapi_configs(self, context: ExecutionContext) -> None:
        """Create FastAPI configuration files."""
        # requirements.txt
        requirements = [
            "fastapi[all]>=0.104.0",
            "uvicorn[standard]>=0.24.0",
            "sqlalchemy>=2.0.0",
            "alembic>=1.12.0",
            "pydantic>=2.4.0",
            "pydantic-settings>=2.0.0",
            "python-jose[cryptography]>=3.3.0",
            "passlib[bcrypt]>=1.7.4",
            "python-multipart>=0.0.6",
            "python-dotenv>=1.0.0",
            "redis>=5.0.0",
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "httpx>=0.25.0",
        ]

        requirements_file = context.project_root / "requirements.txt"
        with open(requirements_file, "w", encoding="utf-8") as f:
            f.write("\n".join(requirements))

        # pyproject.toml
        pyproject_content = f"""[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{context.project_name}"
version = "1.0.0"
description = "Generated by Cursor Development System"
authors = [{{name = "Developer", email = "dev@example.com"}}]
license = {{text = "MIT"}}
requires-python = ">=3.11"

[tool.black]
line-length = 88
target-version = ['py311']
include = '\\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
addopts = "-v --tb=short --strict-markers"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests"
]
"""

        pyproject_file = context.project_root / "pyproject.toml"
        with open(pyproject_file, "w", encoding="utf-8") as f:
            f.write(pyproject_content)

    def _create_python_configs(self, context: ExecutionContext) -> None:
        """Create Python automation configuration files."""
        # requirements.txt
        requirements = [
            "requests>=2.31.0",
            "python-dotenv>=1.0.0",
            "schedule>=1.2.0",
            "click>=8.1.0",
            "rich>=13.5.0",
            "pydantic>=2.4.0",
            "pandas>=2.1.0",
            "openpyxl>=3.1.0",
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ]

        requirements_file = context.project_root / "requirements.txt"
        with open(requirements_file, "w", encoding="utf-8") as f:
            f.write("\n".join(requirements))

    def _create_environment_files(self, context: ExecutionContext) -> None:
        """Create comprehensive environment file structure."""
        # Create .env.example
        env_example_content = f"""# ================================================================
# {context.project_name} - Environment Configuration Template
# ================================================================
# Copy this file to .env and configure your values

# Application Settings
APP_NAME={context.project_name}
APP_ENV=development
APP_DEBUG=true
APP_URL=http://localhost:3000

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME={context.project_name.lower().replace(' ', '_')}
DB_USER=postgres
DB_PASSWORD=your_password_here

# API Configuration
API_VERSION=v1
API_PREFIX=/api
API_RATE_LIMIT=100

# Security
JWT_SECRET=your_jwt_secret_here
JWT_ALGORITHM=HS256
JWT_EXPIRATION=3600

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json
LOG_FILE=logs/app.log

# External Services
REDIS_URL=redis://localhost:6379
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password_here

# Feature Flags
ENABLE_CACHE=true
ENABLE_RATE_LIMITING=true
ENABLE_SWAGGER=true
"""

        env_example_file = context.project_root / ".env.example"
        with open(env_example_file, "w", encoding="utf-8") as f:
            f.write(env_example_content)

        # Create .env.development
        env_dev_content = f"""# ================================================================
# {context.project_name} - Development Environment
# ================================================================

# Application Settings
APP_NAME={context.project_name}
APP_ENV=development
APP_DEBUG=true
APP_URL=http://localhost:3000

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME={context.project_name.lower().replace(' ', '_')}_dev
DB_USER=postgres
DB_PASSWORD=postgres

# API Configuration
API_VERSION=v1
API_PREFIX=/api
API_RATE_LIMIT=1000

# Security
JWT_SECRET=dev_secret_key_change_in_production
JWT_ALGORITHM=HS256
JWT_EXPIRATION=3600

# Logging
LOG_LEVEL=DEBUG
LOG_FORMAT=json
LOG_FILE=logs/app.log

# External Services
REDIS_URL=redis://localhost:6379
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=dev@example.com
SMTP_PASSWORD=dev_password

# Feature Flags
ENABLE_CACHE=true
ENABLE_RATE_LIMITING=false
ENABLE_SWAGGER=true
"""

        env_dev_file = context.project_root / ".env.development"
        with open(env_dev_file, "w", encoding="utf-8") as f:
            f.write(env_dev_content)

    def _create_development_tools(self, context: ExecutionContext) -> None:
        """Create development tools and scripts."""
        # Create scripts directory
        scripts_dir = context.project_root / "scripts"
        scripts_dir.mkdir(exist_ok=True)

        # Create dev.py
        dev_script = '''#!/usr/bin/env python3
"""
Development environment setup and management script.
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Set up development environment."""
    print("Setting up development environment...")

    # Create virtual environment if it doesn't exist
    if not Path(".venv").exists():
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"])

    # Activate virtual environment and install dependencies
    if os.name == "nt":  # Windows
        pip_path = ".venv/Scripts/pip"
    else:  # Unix/Linux/MacOS
        pip_path = ".venv/bin/pip"

    # Install dependencies
    print("Installing dependencies...")
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])

    print("Development environment setup complete!")

def run_tests():
    """Run test suite."""
    print("Running tests...")
    subprocess.run(["pytest", "-v"])

def run_linting():
    """Run code linting."""
    print("Running linting...")
    subprocess.run(["flake8", "src"])
    subprocess.run(["mypy", "src"])

def run_consistency_check():
    """Run codebase consistency validation."""
    print("Running consistency validation...")
    result = subprocess.run(
        [sys.executable, "scripts/validate_consistency.py"]
    )
    if result.returncode != 0:
        print("\\nConsistency validation failed!")
        print("Please fix the issues before continuing.")
        sys.exit(1)
    print("Consistency validation passed!")

def run_all_checks():
    """Run all development checks."""
    print("Running all development checks...")
    run_consistency_check()
    run_linting()
    run_tests()
    print("\\nAll checks completed successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/dev.py "
            "[setup|test|lint|consistency|all]"
        )
        sys.exit(1)

    command = sys.argv[1]
    if command == "setup":
        setup_environment()
    elif command == "test":
        run_tests()
    elif command == "lint":
        run_linting()
    elif command == "consistency":
        run_consistency_check()
    elif command == "all":
        run_all_checks()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
'''

        dev_file = scripts_dir / "dev.py"
        with open(dev_file, "w", encoding="utf-8") as f:
            f.write(dev_script)

        # Create validate.py
        validate_script = '''#!/usr/bin/env python3
"""
Project structure validation script.
"""

import os
import sys
from pathlib import Path
import json

def validate_structure():
    """Validate project structure."""
    print("Validating project structure...")

    # Load project metadata
    with open(".cursor/project.json", "r") as f:
        metadata = json.load(f)

    # Check required directories
    required_dirs = [
        "src",
        "tests",
        "docs",
        "config",
        ".cursor"
    ]

    for dir_name in required_dirs:
        if not Path(dir_name).exists():
            print(f"Error: Required directory '{dir_name}' is missing")
            return False

    # Check required files
    required_files = [
        "README.md",
        ".gitignore",
        ".env.example",
        "requirements.txt"
    ]

    for file_name in required_files:
        if not Path(file_name).exists():
            print(f"Error: Required file '{file_name}' is missing")
            return False

    print("Project structure validation complete!")
    return True

if __name__ == "__main__":
    if not validate_structure():
        sys.exit(1)
'''

        validate_file = scripts_dir / "validate.py"
        with open(validate_file, "w", encoding="utf-8") as f:
            f.write(validate_script)
