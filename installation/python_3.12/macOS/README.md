# Create venv based on 3.12.5

- downlad from https://www.python.org/downloads/release/python-3125/ macOS 64-bit installer and drag and drop `python-3.12.5-macos11.pkg` file to `Application` folder and open it 

- type python and tab to see all available python versions

- find the path to python using
`which python3.12`

- create venv
`python3.12 -m venv python3.12_venv`

- activate venv 
`source python3.12_venv/bin/activate`

- go to `installation/python_3.12/macOS` by 
`cd installation/python_3.12/macOS` and 

- install required libraries with 
`pip install -r requirements.txt`
