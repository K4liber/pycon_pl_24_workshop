## Create venvs based on python 3.13.0rc1

- download installer from https://www.python.org/downloads/release/python-3130rc1/ 

- the Free-threaded Python build is not installed by default. To select it, click on the **Customize** button in the **Installation Type** panel during the install and then check the **Free-Threaded Python package.** 

- please remember the path to the installed pythons

### python3.13_venv

- create venv using python3.13:  
`python3.13 -m venv python3.13_venv`

- activate venv:  
`python3.13_venv\Scripts\activate`

- check if GIL enabled in default (should print "True"):  
`python -c "import sys; print(sys._is_gil_enabled())"`

- install required libraries with:  
`python -m pip install -r installation\requirements.txt`

### python3.13t_venv

- create venv using python3.13t:  
`python3.13t -m venv python3.13t_venv`

- activate venv:  
`python3.13t_venv\Scripts\activate`

- check if GIL enabled in default (should print "False"):  
`python -c "import sys; print(sys._is_gil_enabled())"`

- install required libraries with:  
`python -m pip install -r installation\requirements.txt`
