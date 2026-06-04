# What is this?
This is a collection of code I wrote to deepen my understanding of the different topics taught in TMA4115 - Mathematics 3. 

## How to install and run?
Hopefully I have time to create some notebooks showing how to use this stuff. Stay tuned.

Create and activate a virtual environment, then install the package and its dependencies (including pytest) in editable mode:  
```
python3 -m venv .venv
source venv/bin/activate
pip3 install -e .
pip3 install -r requirements.txt 
```

### Run tests:
Run tests using
```
python3 -m pytest
```

### How to run notebooks:
Easiest way for me to ensure all modules are imported into the notebooks are by creating/installing a dedicated kernel after setting up venv, like so:
```
python3 -m ipykernel install --user --name="MATTE3" --display-name="MATTE3"
```

NB: Make sure to set your kernel to the newly created "MATTE3" kernel:-)