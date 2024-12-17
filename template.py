import os
from pathlib import Path

# workflow
list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txtx",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.py",

]

for filepath in list_of_files:              
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)            # split into filename and filepath
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")