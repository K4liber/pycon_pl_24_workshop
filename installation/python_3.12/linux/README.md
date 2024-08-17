## Create venv based on python 3.12.5

- download the python:  
`wget https://www.python.org/ftp/python/3.12.5/Python-3.12.5.tgz`
- unpack:  
`tar -xf Python-3.12.5.tgz`
- change current directory:  
`cd Python-3.12.5`
- configure:  
`./configure --enable-optimizations`
- build:  
`make -j $(nproc)`
- if the parallel build fails, for some reason it did on my machine:  
`make`
- create env:  
`./python -m venv ~/Desktop/projects/python_venvs/python_3.12.5`
- run python:  
`~/Desktop/projects/python_venvs/python_3.12.5/bin/python`

## Install requirements (please, do not do it right away, it takes long time to finish)

`~/Desktop/projects/python_venvs/python_3.12.5/bin/python -m pip install -r requirements.txt`
