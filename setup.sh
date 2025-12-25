#!/bin/bash
set -e

echo "Step 1: Creating virtual environment..."
python3 -m venv .venv

echo "Step 2: Activating virtual environment..."
source .venv/bin/activate

echo "Step 3: Upgrading pip..."
python -m pip install --upgrade pip

echo "Step 4: Installing Python dependencies..."
python -m pip install -r backend/requirements.txt

echo "Step 5: Checking Tesseract..."
if ! command -v tesseract &> /dev/null
then
    echo "Tesseract not found. Installing via Homebrew..."
    brew install tesseract
else
    echo "Tesseract already installed."
fi

echo "Setup complete!"
echo "You can now run the backend:"
echo "  cd backend && uvicorn main:app --reload"
echo "Then open frontend/index.html in a browser."
