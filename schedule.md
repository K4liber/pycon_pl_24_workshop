## Multi-core processing in Python using Per-interpreter GIL

### Part 1. Concurrency vs parallelism
(slides)
...

### Part 2. Timeline in CPython parallelism context
(background timeline on each slide in this part)
- 1991 -> Initial release on Python
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
- Python (Python language specification, The Python Language Reference, Full Grammar specification) vs CPython

Python is defined partly by its documentation, and partly by its "reference implementation" called CPython. 

- Python interpreter
- GIL
-- ease of programming vs performance
-- dynamic types -> slow execution
-- automation of memory management (reference count) -> GIL
- GIL free implementations (PyPy, IronPython)
- python 3.11 -> 3.12 GIL relocation (image gil_place.png, subinterpreters.png)

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
- `python 3.12.4`
-- try with miniconda
-- check on windows (checked -> works), ubuntu (not yet), mac os (not yet)
- `python 3.13.0b3` ([Free threaded python](https://dev.to/hugovk/help-us-test-free-threaded-python-without-the-gil-1hgf))
#### Windows
- download `Python 3.13.0b3` installer from https://www.python.org/downloads/windows/
- why on JBIEL PC the CPUs were not been fully unitilized while running a command line version of fibonacci test (repo `subinterpreters`)? Test it again.
- test the repo https://github.com/tonybaloney/subinterpreter-web . It does not work on Linux (after executing `make run` we get `Aborted (core dumped)`).
#### Linux
```
git clone https://github.com/K4liber/cpython
git checkout 3.13.0b3
./configure --with-pydebug --disable-gil
make clean
make
./python -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
./python -c "import sys; print(sys._is_gil_enabled())"
./python -m venv <python_3.13_venv_path>
```
- python 3.12.4
```
git clone https://github.com/K4liber/subinterpreters
conda env create
```
### Part 6. Exercieses

### 1. GIL - reference count on a shared state
### 2. GIL - illusional thread safety
### GIL disabled (py3.13t) (TODO simple zadanko)
### Desktop application (threads, multiprocessing, subinterpreters)
### Web server (threads, multiprocessing, subinterpreters) (FastAPI, single process ASGI unicorn)
