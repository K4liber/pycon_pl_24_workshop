# Create venv based on 3.13

## Create python3.13_venv
- downlad from https://www.python.org/downloads/release/python-3130rc1/ macOS 64-bit installer and drag and drop `python-3.13.0b2-macos11.pkg` file to `Application` folder and open it 

- The Free-threaded Python package is not installed by default. To select it, click on the **Customize** button in the **Installation Type** panel during the install and then click to select the **Free-Threaded Python package.** 

- type python and tab to see all available python versions

- create venv using python3.13t and using
`python3.13t -m venv python3.13t_venv`

- activate venv 
`source python3.13t_venv/bin/activate`

- install required libraries with 
`pip install -r installation/requirements.txt`

## Create python3.13t_venv with same steps
`python3.13 -m venv python3.13_venv`
`source python3.13t_venv/bin/activate`
`pip install -r installation/requirements.txt`
