import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:' )

project_name = 'cnnClassifier'

list_of_file=[
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/utils/__init__.py',
    'src/config/__init__.py',
    'src/pipeline/__init__.py',
    'src/entity/__init__.py',
    'src/constants/__init__.py'
    'config/config.yaml',
    'requirements.txt',
    'params.yaml',
    'setup.py',
    'researech/trails.ipynb',
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"creating dir: {filedir} for file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass #creating empty file
            logging.info(f'creating empty file: {filepath}')
    else:
        logging.info(f"{filename} is already exsit")