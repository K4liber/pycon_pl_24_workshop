@REM Provide the python executable path installed locally.
SET Python313Path="C:\Users\kamka\AppData\Local\Programs\Python\Python313\python3.13t"
call %Python313Path% -m venv .py313tvenv
call .py313tvenv\Scripts\activate
call pip install -r requirements_excercise_5.txt