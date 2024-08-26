## Create venv based on python 3.12.5

- download Python-3.12.5:  
`wget https://www.python.org/ftp/python/3.12.5/Python-3.12.5.tgz`
- unpack:  
`tar -xf Python-3.12.5.tgz`
- change current directory:  
`cd Python-3.12.5`
- configure:  
`./configure --enable-optimizations`
- build:  
`make -j $(nproc)`
- create venv (create venv in the root directory of the `pycon_pl_24_workshop` repository using the python build in the current directory):  
`./bin/python -m venv <path_to_pycon_pl_24_workshop_repositore>/python3.12_venv`  
- go to the root directory of the `pycon_pl_24_workshop` repository  
- run python (just a check if it works, should print "3.12.5 ..."):  
`python3.12_venv/bin/python -c "import sys; print(sys.version)"`
- install requirements:  
`python3.12_venv/bin/python -m pip install -r installation/python_3.12/linux/requirements.txt`
