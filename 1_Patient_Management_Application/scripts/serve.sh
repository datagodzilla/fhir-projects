#!/bin/bash
# HealthPlus Patient Management Application - Local Development Server
# Starts a Python HTTP server and opens the app in the default browser.

PORT=${1:-8080}
DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "Starting HealthPlus Patient Management Application..."
echo "Serving from: $DIR"
echo "URL: http://localhost:$PORT"
echo "Press Ctrl+C to stop."
echo ""

# Open browser after a short delay
(sleep 1 && open "http://localhost:$PORT/patient_management_app.html" 2>/dev/null || xdg-open "http://localhost:$PORT/patient_management_app.html" 2>/dev/null) &

# Start server
cd "$DIR" && python3 -m http.server "$PORT"
