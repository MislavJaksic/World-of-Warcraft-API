"""
    Adds "src" to sys.path.

    Now you can do imports with "from wowapi.Sub-Package ...".
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
