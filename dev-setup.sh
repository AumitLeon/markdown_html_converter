echo "Install development dependencies..."
pip install -r requirements-dev.txt

echo "Install pre-commit git hooks"
pre-commit install