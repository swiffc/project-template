# Cursor Development System

A powerful project scaffolding tool that helps developers create and manage projects with best practices and modern architecture patterns.

## Features

- 🏗️ **Project Templates**: Pre-configured templates for various project types
- 🔧 **Smart Configuration**: Automatic setup of development tools and dependencies
- 📁 **Directory Structure**: Industry-standard project layouts
- 🤖 **AI Integration**: Optimized for Cursor AI with smart rules and context
- 🎯 **Complexity-Based Development**: Phased approach to project development
- 🔍 **Validation**: Built-in project structure validation
- 🛠️ **Development Tools**: Integrated scripts for common tasks

## Supported Project Types

- React SPA
- Next.js Fullstack
- Vue + Nuxt
- Express API
- FastAPI Backend
- Electron Desktop
- React Native
- Flutter Mobile
- Python Automation
- Windows Automation
- CAD Automation
- AI/ML Project
- Static Website

## Installation

```bash
pip install cursor-dev-system
```

## Quick Start

Create a new project:

```bash
cursor-dev my-project --type react-spa
```

Available options:

```bash
cursor-dev --help
```

## Development Phases

The system follows a complexity-based development approach:

1. **Architecture Phase** (Highest Complexity)
   - Database schema and core models
   - Authentication and security systems
   - Core business logic and algorithms
   - System architecture decisions

2. **API Layer** (High Complexity)
   - REST/GraphQL API endpoints
   - Data validation and serialization
   - Error handling and middleware
   - Service layer implementation

3. **UI Layer** (Medium Complexity)
   - User interface components
   - Forms and user interactions
   - Navigation and routing
   - State management

4. **Polish Phase** (Low Complexity)
   - Styling and visual design
   - Performance optimization
   - Testing and documentation
   - Deployment configuration

## Project Structure

```text
project/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration
└── .cursor/       # AI configuration
```

## Development Tools

The system provides several development tools:

```bash
# Set up development environment
python scripts/dev.py setup

# Run tests
python scripts/dev.py test

# Run linting
python scripts/dev.py lint

# Validate project structure
python scripts/validate.py
```

## Configuration

The system can be configured through:

- Command line arguments
- Environment variables
- Configuration files
- Project metadata

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cursor AI](https://cursor.sh) for the amazing development environment
- All contributors who have helped shape this project
