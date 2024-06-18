0. Prepare python environments
- python3.12
- python3.13t [(](https://dev.to/hugovk/help-us-test-free-threaded-python-without-the-gil-1hgf))

1. Why GIL? History background (5 minutes)
- slides

2. Practical cases where GIL is needed
3. Practical cases with GIL disabled (py3.13t)
4. -||- with desktop application (threads, multiprocessing, subinterpreters)
5. -||- with web server (threads, multiprocessing, subinterpreters) (e.g. FastAPI wsgi)
