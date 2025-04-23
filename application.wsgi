#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WSGI entry point for a Flask application stored in a single repository folder with just `app.py` and `requirements.txt`.
Place this `application.wsgi` in the same folder after cloning your GitHub repo.
"""
import sys
import logging
import os

# Enable logging to stderr for debugging
logging.basicConfig(stream=sys.stderr)

# Automatically set the project path to this file's directory
project_path = os.path.dirname(__file__)
sys.path.insert(0, project_path)

# (Optional) Activate a virtual environment located in `venv/`
# Uncomment and adjust if you have one:
# venv_path = os.path.join(project_path, 'venv', 'bin', 'activate_this.py')
# with open(venv_path) as f:
#     exec(f.read(), { '__file__': venv_path })

# Import your Flask app from app.py
# Ensure app.py defines `app = Flask(__name__)`
from app import app as application
