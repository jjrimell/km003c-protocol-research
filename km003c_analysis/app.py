"""
Main entry point for the KM003C Analysis application.

This module provides the main Streamlit GUI for analyzing KM003C USB protocol captures.
The actual implementation is in the dashboards.main module.
"""

# Import and run the main dashboard
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from km003c_analysis.dashboards.main import main

if __name__ == "__main__":
    main()

# This allows the app to be run with: streamlit run km003c_analysis/app.py
# or: uv run python -m streamlit run km003c_analysis/app.py