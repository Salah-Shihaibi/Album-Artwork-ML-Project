find . -type f -not -path "./venv/*" -name "*.py" | xargs pylint
