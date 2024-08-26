# Create venv based on 3.13

- downlad from https://www.python.org/downloads/release/python-3130rc1/  windows 64-bit installer

- The Free-threaded Python package is not installed by default. To select it, click on the **Customize** button in the **Installation Type** panel during the install and then click to select the **Free-Threaded Python package.** 


- create venv using python3.13t
`python3.13t -m venv python3.13t_venv`

- activate venv 
`python3.13t_venv/Scripts/activate`

- install required libraries with 
`pip install -r requirements.txt`
