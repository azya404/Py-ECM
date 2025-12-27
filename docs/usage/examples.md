# Common Use Cases

Real-world examples of using Py-ECM.

## Student: Taking Class Notes
```bash
# Create course folder structure
mkdir -p ~/Documents/CS101

# Create lecture notes
py-ecm create lecture-01.md --dir ~/Documents/CS101 --content "# Lecture 1: Introduction"

# Create assignment file
py-ecm create hw1.txt --dir ~/Documents/CS101 --content "Problem set 1"
```

## Developer: Project Setup
```bash
# Initialize project files
py-ecm create README.md --content "# My Project"
py-ecm create .gitignore --content "node_modules/\n*.log"
py-ecm create main.py --content "def main():\n    print('Hello')"
```

## Office Worker: Daily Reports
```bash
# Create timestamped report
py-ecm create "report-2024-12-27.txt" --dir ~/Documents/Reports

# Create template
py-ecm create template.txt --content "Date:\nProject:\nStatus:\nNotes:"
```

## Batch File Creation
```bash
# Create multiple config files
py-ecm create .env --content "API_KEY=placeholder"
py-ecm create config.json --content '{}'
py-ecm create settings.yaml --content 'version: 1.0'
```