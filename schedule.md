## Multi-core processing in Python using Per-interpreter GIL

### Part 1. Concurrency vs parallelism
(slides)
...

### Part 2. Timeline in CPython parallelism context
(background timeline on each slide in this part)
- 1991 -> Initial release on Python
- 1994 -> Initial realese of CPython
- 1997 -> CPython users can run multiple interpreters in the same process (https://docs.python.org/3/c-api/init.html#sub-interpreter-support)
- ...
- 2001 -> the world’s first multicore processor "Power4"
- 2016 -> Gilectomy, partially successful attempt to remove the GIL from CPython
- 2017 -> PEP 554 – Multiple Interpreters in the Stdlib
- 2022 -> PEP 684 – A Per-Interpreter GIL
- 2023 -> PEP 703 – Making the Global Interpreter Lock Optional in CPython
- 2023 -> PEP 734 – Multiple Interpreters in the Stdlib
- 2024 -> Python 3.13 released with Per-Interpreter GIL and free-threading

(slides)
- Python vs CPython
- Python interpreter
- GIL
- GIL free implementations (PyPy, IronPython)

### Part 3. Concurrency in Python
- multithreading
- asyncio
- multiprocessing

### Part 4. Parallelism related concepts in Python
- multiprocessing
- web servers options: ASGI (gunicorn)/containers
- (NEW in 3.13!) Per-interpreter GIL
- (NEW in 3.13!) Free Threading (https://docs.python.org/3.13/howto/free-threading-extensions.html)

### Part 5. Prepare python environments
- python3.12.4
-- try with miniconda
-- check on windows (checked -> works), ubuntu (not yet), mac os (not yet)
- python3.13t ([Free threaded python](https://dev.to/hugovk/help-us-test-free-threaded-python-without-the-gil-1hgf))
#### Windows
-- install without any requirements and addapt the code to not import any requirements (py313t)
-- why on JBIEL PC the CPUs were not been fully unitilized?
#### Linux
- python 3.13.0b3
```
git clone https://github.com/K4liber/cpython
git checkout 3.13.0b3
./configure --with-pydebug --disable-gil
make clean
make
/python.exe -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
./python -c "import sys; print(sys._is_gil_enabled())"
./python -m venv <python_3.13_venv_path>
```
- python 3.12.4
```
git clone https://github.com/K4liber/subinterpreters
conda env create
```
### Part 6. Practical cases

### GIL saves the day
### GIL disabled (py3.13t)
### Desktop application (threads, multiprocessing, subinterpreters)
### Web server (threads, multiprocessing, subinterpreters) (FastAPI, single process ASGI unicorn)
