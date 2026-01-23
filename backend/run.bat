@echo off
cd /d "C:\Users\zaid shaikh\OneDrive\Desktop\sports-portal-supabase\backend"
echo ========================================
echo 🚀 Sports Portal - Starting Application
echo ========================================
echo Installing Python dependencies...
pip install -q -r requirements.txt
echo.
echo Seeding database with test users...
python seed_db.py
echo.
echo 🌐 Starting Flask server on http://localhost:5000
echo Press Ctrl+C to stop
echo ========================================
python app.py
pause