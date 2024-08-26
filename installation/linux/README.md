## Create venvs based on python 3.13.0rc1

### python3.13_venv

- clone the source code of the python 3.13 release candidate (please clone it outside the `pycon_pl_24_workshop` repository):  
`git clone --depth 1 --branch v3.13.0rc1 https://github.com/python/cpython`
- change current directory:  
`cd cpython`
- configure:  
`./configure --enable-optimizations`
- build:  
`make -j $(nproc)`
- create venv (create venv in the root directory of the `pycon_pl_24_workshop` repository using the python build in the current directory):  
`./python -m venv <path_to_pycon_pl_24_workshop_repositore>/python3.13_venv`  
- go to the root directory of the `pycon_pl_24_workshop` repository
- check if GIL enabled in default (should print "True"):  
`python3.13_venv/bin/python -c "import sys; print(sys._is_gil_enabled())"`
- install requirements:  
`python3.13_venv/bin/python -m pip install -r installation/linux/requirements.txt`

### python3.13t_venv

- clone the source code of the python 3.13 release candidate (please clone it outside the `pycon_pl_24_workshop` repository):  
`git clone --depth 1 --branch v3.13.0rc1 https://github.com/python/cpython`
- change current directory:  
`cd cpython`
- configure:  
`./configure --disable-gil --enable-optimizations`
- build:  
`make -j $(nproc)`
- create venv (create venv in the root directory of the `pycon_pl_24_workshop` repository using the python build in the current directory):  
`./python -m venv <path_to_pycon_pl_24_workshop_repositore>/python3.13t_venv`  
- go to the root directory of the `pycon_pl_24_workshop` repository
- check if GIL enabled in default (should print "False"):  
`python3.13t_venv/bin/python -c "import sys; print(sys._is_gil_enabled())"`
- check if GIL enabled while providing `Xgil=1` flag (should print "True"):  
`python3.13t_venv/bin/python -Xgil=1 -c "import sys; print(sys._is_gil_enabled())"`
- install requirements:  
`python3.13t_venv/bin/python -m pip install -r installation/linux/requirements.txt`
