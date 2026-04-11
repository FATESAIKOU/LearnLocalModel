#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo "Stopping services..."
    # Kill the background backend process
    if [ -n "$BACKEND_PID" ]; then
        kill $BACKEND_PID
        echo "Backend stopped."
    fi
    # Kill any remaining node processes related to the frontend
    pkill -f "react-scripts"
    echo "Frontend stopped."
    exit
}

# Trap SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

echo "Starting Fullstack Todo Application..."

# 1. Setup Backend
echo "Setting up Backend..."
cd backend
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
# Start backend in background
python main.py &
BACKEND_PID=$!
cd ..

# Give the backend a few seconds to initialize
echo "Waiting for backend to start..."
sleep 5

# 2. Setup Frontend
echo "Setting up Frontend..."
cd frontend
if [ ! -d "node_modules" ]; then
    npm install
fi
# Start frontend
npm start &
FRONTEND_PID=$!
cd ..

# Keep the script running so the trap can catch Ctrl+C
echo "Both services are running. Press Ctrl+C to stop everything."
wait $BACKEND_PID $FRONTEND_PID
