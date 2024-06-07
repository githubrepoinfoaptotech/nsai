import os
import sys

# Insert the project directory into the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Import your Flask app
from app import app as application  # Ensure 'app' matches your Flask app instance name in app.py
