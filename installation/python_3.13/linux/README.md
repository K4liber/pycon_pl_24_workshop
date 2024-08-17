## Create venv based on python 3.13.0rc1

- clone the source code of the python 3.13 release candidate:  
`git clone --depth 1 --branch v3.13.0rc1 https://github.com/python/cpython`
- change current directory:  
`cd cpython`
- configure:  
`./configure --disable-gil --enable-optimizations`
- build:  
`make -j $(nproc)`
- create env:  
`./python -m venv ~/Desktop/projects/python_venvs/python_3.13.0`
- run python 3.13.0 (GIL disabled in default):  
`~/Desktop/projects/python_venvs/python_3.13.0/bin/python`
- run python 3.13.0 with GIL enabled:  
`PYTHON_GIL=1 ~/Desktop/projects/python_venvs/python_3.13.0/bin/python`

## Install requirements (please, do not do it right away, it takes long time to finish)

`~/Desktop/projects/python_venvs/python_3.13.0/bin/python -m pip install -r requirements.txt`
