import os
from pathlib import Path
import logging

# workflow process
# 1. update config.yaml
# 2. update secrets.yaml
# 3. update params.yaml
# 4. update the entity
# 5. update the configuration manager in src config
# 6. update the components
# 7. update the pipeline
# 8. update the main.py
# 9. update the dvc.yaml
# 10. app.py

# logging screen
def get_logger():
    logger = logging.getLogger("CNN_classifier")
    return logger


project_name = "CNN_clasifier"
logger = get_logger()

# list of files that this template creates
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "test.py",
]

# creating folders and empty files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"creating directory {filedir} for {filename}")

    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logger.info(f"creating an empty file {filename}")

    else:
        logger.info(f"{filename} already exists")
