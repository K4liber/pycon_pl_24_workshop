## Multi-core processing in Python using Per-interpreter GIL

### Part 1. Concurrency vs parallelism

(TODO slides)

### Part 2. Timeline in CPython parallelism context

(background timeline on each slide in this part)
- 1991 -> Initial release on Python
- 1997 -> CPython users can run multiple interpreters in the same process (https://docs.python.org/3/c-api/init.html#sub-interpreter-support)
- ...
- 2001 -> The world’s first multicore processor "Power4"
- 2016 -> Gilectomy, partially successful attempt to remove the GIL from CPython
- 2017 -> PEP 554 – Multiple Interpreters in the Stdlib
- 2022 -> PEP 684 – A Per-Interpreter GIL
- 2023 -> PEP 703 – Making the Global Interpreter Lock Optional in CPython
- 2023 -> PEP 734 – Multiple Interpreters in the Stdlib
- 2024 -> Python 3.13 released with Per-Interpreter GIL and free-threading

### Part 3. GIL -> simple solution for reference counting in CPython

- Python (Python language specification, The Python Language Reference, Full Grammar specification) vs CPython

Python is defined partly by its documentation, and partly by its "reference implementation" called CPython. 

- Python interpreter
- GIL
-- ease of programming vs performance
-- dynamic types -> slow execution
-- automation of memory management (reference counting) -> GIL
- GIL free implementations (PyPy, IronPython) -> how those impelmentation exist without reference counting?

"The garbage collectors used or implemented by PyPy are not based on reference counting, so the objects are not freed instantly when they are no longer reachable. The most obvious effect of this is that files (and sockets, etc) are not promptly closed when they go out of scope. For files that are opened for writing, data can be left sitting in their output buffers for a while, making the on-disk file appear empty or truncated. Moreover, you might reach your OS’s limit on the number of concurrently opened files."

-> Once more, GIL prevent a developer to care about some aspects of memory management described above.

- python 3.11 -> 3.12 GIL relocation (image gil_place.png, subinterpreters.png)

### Part 4. Concurrency in Python

- multithreading
- asyncio
- multiprocessing

### Part 5. Parallelism related concepts in Python
(add the image with visualization similar to images/gil_place.png)

- multiprocessing
- web server with multi-workers: ASGI (gunicorn)
- (NEW in 3.13!) Per-interpreter GIL (subinterpreters)
- (NEW in 3.13!) Free threading - multi-threading without GIL (https://docs.python.org/3.13/howto/free-threading-extensions.html)

### Part 6. Prepare python environments

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
./configure --disable-gil --enable-optimizations
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

### Part 7. Exercieses

#### 1. GIL - reference count on a shared state
#### 2. GIL - illusional thread safety
#### 3. GIL disabled (python 3.13  --disable-gil)
#### (TODO) Desktop application (threads, multiprocessing, subinterpreters)
#### (TODO) Web server (threads, multiprocessing, subinterpreters) (FastAPI, single process ASGI unicorn)
