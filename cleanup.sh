#!/bin/bash

echo "Cleaning up processes..."

# Kill backend python process
pkill -f "python main.py"

# Kill frontend node/react process
pkill -f "react-scripts"

echo "Cleanup complete."
