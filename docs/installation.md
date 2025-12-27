# Installation Guide

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

### From Source (Current)
```bash
# Clone the repository
git clone https://github.com/azya404/Py-ECM.git
cd Py-ECM

# Install in development mode
pip install -e .
```

### Verify Installation
```bash
py-ecm version
# Output: Py-ECM v0.1.0
```

## From PyPI (Coming Soon)
```bash
pip install py-ecm
```

## Troubleshooting

### Command not found

If `py-ecm` command isn't recognized after installation:

**Windows:**
- Ensure Python Scripts directory is in PATH
- Try `python -m py_ecm.cli` instead

**Mac/Linux:**
- Ensure `~/.local/bin` is in PATH
- Try reinstalling: `pip install --force-reinstall -e .`

### Permission errors

Use `--user` flag if you don't have admin rights:
```bash
pip install --user -e .
```