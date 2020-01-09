# install virtualenv with python 3 
virtualenv -p python3 .venv

# setup created virtualenv
source .venv/bin/activate

# clone the package fo GMatch4py from the repository:
https://github.com/Jacobe2169/GMatch4py.git

# put the package to the following directory:
venv/lib/python3.6/site_packages

# cd to the directory above and install gmatch4py:
pip install .

# install other requirements in requirements.txt file 
pip install -r requirements.txt