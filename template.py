import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    ".github/workflows/.gitkeep",
    ".env",
    "data/.gitkeep",
    "data_models/__init__.py",
    "research/trials.ipynb",
    "prompt_library/__init__.py",
    "toolkit/__init__.py",
    "utils/__init__.py",
    "main.py",
    "agent.py",
    "streamlit_app.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")    
    else:
        logging.info(f"File already exists: {filename}")