# Automated Setup Script for Work Tracker

## Quick Start (Windows)

Run this script to automate the initial setup:

```powershell
# Save this as setup.ps1 and run it

# Create and activate virtual environment
python -m venv worklog
.\worklog\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Copy environment template
Copy-Item config/.env.example .env

# Prompt user to configure database
Write-Host "================================================"
Write-Host "IMPORTANT: Configure your database connection"
Write-Host "================================================"
Write-Host ""
Write-Host "1. Go to https://neon.tech and create a free account"
Write-Host "2. Create a new project"
Write-Host "3. Copy your connection string"
Write-Host "4. Edit the .env file and paste your DATABASE_URL"
Write-Host ""
Write-Host "Press any key when you've added your DATABASE_URL to .env..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Initialize database migrations
Write-Host ""
Write-Host "Initializing database migrations..."
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Write-Host ""
Write-Host "================================================"
Write-Host "Setup complete! Run the app with: python -m app"
Write-Host "================================================"
```

## Quick Start (macOS/Linux)

Run this script to automate the initial setup:

```bash
#!/bin/bash
# Save this as setup.sh and run: bash setup.sh

# Create and activate virtual environment
python3 -m venv worklog
source worklog/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp config/.env.example .env

# Prompt user to configure database
echo "================================================"
echo "IMPORTANT: Configure your database connection"
echo "================================================"
echo ""
echo "1. Go to https://neon.tech and create a free account"
echo "2. Create a new project"
echo "3. Copy your connection string"
echo "4. Edit the .env file and paste your DATABASE_URL"
echo ""
read -p "Press Enter when you've added your DATABASE_URL to .env..."

# Initialize database migrations
echo ""
echo "Initializing database migrations..."
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

echo ""
echo "================================================"
echo "Setup complete! Run the app with: python -m app"
echo "================================================"
```

## Syncing to Another Laptop

```powershell
# Windows PowerShell
git clone <your-repo-url>
cd Work-Tracker
python -m venv worklog
.\worklog\Scripts\Activate.ps1
pip install -r requirements.txt

# Create .env file with your DATABASE_URL
Copy-Item config/.env.example .env
# Edit .env with your database credentials

# Run the app
python -m app
```

## GitHub Actions (Future Enhancement)

You can add automated testing with GitHub Actions by creating `.github/workflows/test.yml`:

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest tests/
```
