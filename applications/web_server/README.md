Exercise based on subinterpreter web server implementation by Anthony Shaw
(https://github.com/tonybaloney/subinterpreter-web)

### I. Turn on webserver.

- change current directory:  
`cd applications/web_server`  
- run selected web-server:   
1. multi-threads (please use python3.13_venv):
```
python -m hypercorn -w1 flask_app:app
```
2. multiprocesses (please use python3.13_venv):
```
python -m hypercorn -w8 flask_app:app
```
3. subinterpreters (please use python3.13_venv):
```
python subinterpreter_web.py -w 8 flask_app:app
```
4. free-threading (please use python3.13t_venv):
```
python -Xgil=0 -m hypercorn -w1 flask_app:app
```

### II. Test sending multiple requests to the web-server under one case scenario
(multi-threads, multiprocesses, subinterpreters, free-threading )

```
python test_web_server.py
```

###. III. Compare the results. Take a look at the PID/TID from the response text.

### Test results on LINUX

Linux 5.15.0-58-generic #64~20.04.1-Ubuntu x86_64 x86_64 x86_64 GNU/Linux  
CPUs = 2

```
python3.13t -m hypercorn -Xgil=1 -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 17 2024, 14:38:31) [GCC 9.4.0])
INFO: 40 tasks executed in 176.43s
```
```
python3.13 -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 85.28s
```
```
python3.13 -m hypercorn -w8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 40.61s
```
```
python3.13 subinterpreter_web.py -w 8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 40.03s
```
```
python3.13t -Xgil=0 -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL disabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 09:52:40) [GCC 9.4.0])
INFO: 40 tasks executed in 67.69s
```

Windows 
CPUs = 8

```
python -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 20:58:38) [MSC v.1940 64 bit (AMD64)])
INFO: 40 tasks executed in 31.31s

python -m hypercorn -w8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 20:58:38) [MSC v.1940 64 bit (AMD64)])
INFO: 40 tasks executed in 11.18s

python.exe subinterpreter_web.py -w 8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 20:58:38) [MSC v.1940 64 bit (AMD64)])
INFO: 40 tasks executed in 10.98s

..\..\python3.13t_venv\Scripts\python.exe -Xgil=0 -m hypercorn -w1 flask_app:app
Cannot import flask! What now?

```