#!/bin/sh

# Start game in background
python3 /reverse_ai/main.py &
# Start Flask server
python3 /reverse_ai/server.py