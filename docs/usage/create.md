# File Creation Guide

Create new files with optional content and custom locations.

## Basic Usage
```bash
py-ecm create FILENAME [OPTIONS]
```

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--dir` | `-d` | Target directory | Current directory |
| `--content` | `-c` | Initial file content | Empty file |

## Examples

### Create Empty File
```bash
py-ecm create report.txt
```
**Output:** `✓ Created: C:\Users\...\report.txt`

### Create File with Content
```bash
py-ecm create notes.txt --content "Meeting notes from today"
```

### Create in Specific Directory
```bash
# Absolute path
py-ecm create todo.txt --dir C:\Users\azya\Documents

# Relative path
py-ecm create ideas.txt --dir ./projects

# Home directory (Unix-style)
py-ecm create memo.txt --dir ~/Desktop
```

### Using Short Flags
```bash
py-ecm create shopping.txt -d ~/Desktop -c "Buy eggs and milk"
```

### Different File Types
```bash
# Python script
py-ecm create script.py --content "print('Hello World')"

# JSON data
py-ecm create data.json --content '{"name": "test"}'

# Markdown document
py-ecm create README.md --content "# My Project"

# No extension
py-ecm create Makefile --content "all:\n\techo 'Building...'"
```

### Files with Spaces
```bash
py-ecm create "my document.txt" --content "Important notes"
```

## Error Handling

### File Already Exists
```bash
py-ecm create existing.txt
# ✗ File already exists: existing.txt
# Exit code: 1
```

### Directory Not Found
```bash
py-ecm create file.txt --dir /nonexistent
# ✗ Directory does not exist: /nonexistent
# Exit code: 1
```

### Permission Denied
```bash
py-ecm create test.txt --dir C:\Windows\System32
# ✗ Permission denied: C:\Windows\System32\test.txt
# Exit code: 1
```

### Target is Directory
```bash
py-ecm create existing_folder
# ✗ 'existing_folder' is a directory
# Exit code: 1
```

## Tips

- Use quotes around filenames with spaces
- Paths can be absolute or relative
- Content supports escape sequences: `\n` for newlines
- Exit codes: 0 = success, 1 = error