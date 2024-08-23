@REM Provide the python executable path installed locally.
SET Python313Path="C:\Users\kamka\AppData\Local\Programs\Python\Python313\python3.13t"
call %Python313Path% -m venv python3.13t_venv
call python3.13t_venv\Scripts\activate
call cd installation\python_3.13\windows
call pip install -r requirements.txt