Exercise based on subinterpreter web server implementation by Anthony Shaw
(https://github.com/tonybaloney/subinterpreter-web)

### I. Turn on webserver.

<!-- 0. change current directory:   -->
<!-- `cd applications/web_server`   -->
- run selected web-server:   
1. multi-threads (please use python3.13_venv):
```
python -m hypercorn -w1 applications/web_server/flask_app:app
```
2. multiprocesses (please use python3.13_venv):
```
python -m hypercorn -w8 applications/web_server/flask_app:app
```
3. subinterpreters (please use python3.13_venv):
```
python subinterpreter_web.py -w 8 flask_app:app
```
4. free-threading (please use python3.13t_venv):
```
python -Xgil=0 -m hypercorn -w1 applications/web_server/flask_app:app
```

### II. Test sending multiple requests to the web-server under one case scenario
(multi-threads, multiprocesses, subinterpreters, free-threading )

0. open new terminal, remember to activate the virtual env
0. change current directory:  
<!-- `cd applications/web_server`   -->
```
python applications/web_server/test_web_server.py
```

###. III. Compare the results. Take a look at the PID/TID from the response text.

### Test results on LINUX

Linux 5.15.0-58-generic #64~20.04.1-Ubuntu x86_64 x86_64 x86_64 GNU/Linux  
CPUs = 2

```
python -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 17 2024, 14:38:31) [GCC 9.4.0])
INFO: 40 tasks executed in 176.43s
```
```
python -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 85.28s
```
```
python -m hypercorn -w8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 40.61s
```
```
python subinterpreter_web.py -w 8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 40.03s
```
```
python -Xgil=0 -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL disabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 09:52:40) [GCC 9.4.0])
INFO: 40 tasks executed in 67.69s
```


### Test results on macOS

1. multi-threads GIL enabled
`
python -m hypercorn -w1 applications/web_server/flask_app:app
python applications/web_server/test_web_server.py
INFO: Testing server: (GIL enabled) 3.13.0rc1 (v3.13.0rc1:e4a3e786a5e, Jul 31 2024, 19:49:53) [Clang 15.0.0 (clang-1500.3.9.4)]) INFO: 40 tasks executed in 41.72s
`ś


2. multi-processing
`
python -m hypercorn -w8 applications/web_server/flask_app:app
python applications/web_server/test_web_server.py
INFO: Testing server: (GIL enabled) 3.13.0rc1 (v3.13.0rc1:e4a3e786a5e, Jul 31 2024, 19:49:53) [Clang 15.0.0 (clang-1500.3.9.4)])
INFO: 40 tasks executed in 9.72s
`

3. subinterpreters 
`
cd applications/web_server
python subinterpreter_web.py -w 8 flask_app:app
INFO: Starting 8 subinterpreter workers
`
new terminal
python applications/web_server/test_web_server.py
INFO: Testing server: (GIL enabled) 3.13.0rc1 
INFO: 40 tasks executed in 12.86s


4. 
free-threading (GIL disabled)
`
python -Xgil=0 -m hypercorn -w1 applications/web_server/flask_app:app 
python applications/web_server/test_web_server.py 
INFO: Testing server: (GIL disabled) 3.13.0rc1 experimental free-threading build (v3.13.0rc1:e4a3e786a5e, Jul 31 2024, 19:57:27) [Clang 15.0.0 (clang-1500.3.9.4)])
INFO: 40 tasks executed in 16.58s
`