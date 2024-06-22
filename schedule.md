### Prepare python environments
- python3.12
- python3.13t ([Free threaded python](https://dev.to/hugovk/help-us-test-free-threaded-python-without-the-gil-1hgf))

### Concurrency vs parallelism
...
### Concurrency in Python
- multithreading
- asyncio
- multiprocessing

### Parallelism in Python
- multiprocessing
- web servers options: ASGI (gunicorn)/containers
- (NEW in 3.13!) Per-interpreter GIL
- (NEW in 3.13!) Free Threading (https://docs.python.org/3.13/howto/free-threading-extensions.html)

### Why GIL exists? Historical background (5 minutes)
- slides

# Practical cases

### GIL saves the day
### GIL disabled (py3.13t)
### Desktop application (threads, multiprocessing, subinterpreters)
### Web server (threads, multiprocessing, subinterpreters) (FastAPI, single process ASGI unicorn)
