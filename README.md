# Py-ECM (Python Enterprise Content Manager)

> CLI-based enterprise content management system demonstrating production-grade software architecture and ECM domain knowledge.

## 🎯 Project Vision

**Current Phase:** Pure Python CLI implementation
**Future Phases:** Web interface → Full-stack platform

This project showcases understanding of enterprise content management systems through iterative development - starting with core business logic in a CLI, then progressively adding web interfaces and advanced features.

## Project Status
**Version:** 0.1.0 (Active Development - CLI Foundations)
This project is under active development
**Current Focus:** Building robust file operations and metadata management via command-line interface.

## Planned Features and Roadmap

### Phase 1: CLI Foundation
- Professional Python package structure
- CLI framework with Typer
- File CRUD operations with pathlib (Create, Read, Update, Delete)
- Metadata tracking and tagging system
- Version control for content items
- Permission and audit logging
- Search and filter capabilities
- Workflow state management

### Phase 2: Data Layer 
- SQLite integration for metadata persistence
- Full-text search capabilities
- Analytics and reporting
- Automated retention policies

### Phase 3: Web Interface 
- Flask/FastAPI REST API
- Lightweight frontend with HTMX
- Document preview capabilities
- User dashboard

### Phase 4: Advanced Features 
- Real-time collaboration
- Visual workflow designer
- Advanced analytics
- Production deployment

## Tecnology Stack

**Core (Phase 1):**
- Python 3.10+ with type hints
- Typer - Professional CLI framework
- pathlib - Cross-platform path handling
- SQLAlchemy - Database ORM (planned)

**Testing & Quality:**
- pytest - Unit testing
- Coverage.py - Code coverage
- Black - Code formatting

**Future Stack:**
- Flask/FastAPI - Web framework
- PostgreSQL - Production database
- React - Modern frontend (stretch goal)

## Installation (Coming Soon)
```bash
# Once published to PyPI
pip install py-ecm

# Development installation
git clone https://github.com/azya404/Py-ECM.git
cd Py-ECM
pip install -e .
```

## Usage (Preview)
```bash
# Check version
py-ecm version

# More commands coming soon... (here's a sneak peak)
# py-ecm create document.txt --tags project,urgent
# py-ecm list --filter status=pending
# py-ecm workflow start approval --document doc.txt
```

## Contributing
Feedback welcome via issues or azya404@users.noreply.github.com

## License
MIT License - see [LICENSE](LICENSE) for details