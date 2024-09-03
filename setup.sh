#!/bin/bash
echo "Setting up the virtual environment..."
python3 -m venv env
source env/bin/activate

echo "Installing backend dependencies..."
pip install -r backend/requirements.txt

echo "Installing frontend dependencies..."
pip install -r frontend/requirements.txt

echo "Setup complete. To run the application:"
echo "1. Activate the virtual environment: source env/bin/activate"
echo "2. Start the backend server: uvicorn backend.app.main:app --reload"
echo "3. Start the frontend app: streamlit run frontend/streamlit_app.py"
