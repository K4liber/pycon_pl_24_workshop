Exercise based on subinterpreter web server implementation by Anthony Shaw
(https://github.com/tonybaloney/subinterpreter-web)

### I. Turn on selected webserver

(please change current working directory to `applications/web_server`)

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
5. (optional) free-threading build with GIL enabled (please use python3.13t_venv and flag -Xgil=1):  
```
python -Xgil=1 -m hypercorn -w1 flask_app:app
```

### II. Test sending multiple requests to the web-server under one case scenario

Test the started server by running (use any python version >= 3.9). Open new terminal and type:
```
python applications/web_server/test_web_server.py
```

### III. Compare the results. Take a look at the PID/TID from the response text.

#### Test results on LINUX
```
Linux 5.15.0-58-generic #64~20.04.1-Ubuntu x86_64 x86_64 x86_64 GNU/Linux  
CPUs = 2
```
1. multi-threads
```
python3.13 -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 85.28s
```
2. multiprocesses
```
python3.13 -m hypercorn -w8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 40.61s
```
3. subinterpreters
```
python3.13 subinterpreter_web.py -w 8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
INFO: 40 tasks executed in 40.03s
```
4. free-threading
```
python3.13t -Xgil=0 -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL disabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 09:52:40) [GCC 9.4.0])
INFO: 40 tasks executed in 67.69s
```
5. free-threading build with GIL enabled
```
python3.13t -m hypercorn -Xgil=1 -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 17 2024, 14:38:31) [GCC 9.4.0])
INFO: 40 tasks executed in 176.43s
```

### Test results on macOS

1. multi-threads
```
python -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (v3.13.0rc1:e4a3e786a5e, Jul 31 2024, 19:49:53) [Clang 15.0.0 (clang-1500.3.9.4)]) 
INFO: 40 tasks executed in 41.72s
```
2. multiprocesses
```
python -m hypercorn -w8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (v3.13.0rc1:e4a3e786a5e, Jul 31 2024, 19:49:53) [Clang 15.0.0 (clang-1500.3.9.4)])
INFO: 40 tasks executed in 9.72s
```
3. subinterpreters 
```
python subinterpreter_web.py -w 8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 
INFO: 40 tasks executed in 12.86s
```
4. free-threading
```
python -Xgil=0 -m hypercorn -w1 flask_app:app 
INFO: Testing server: (GIL disabled) 3.13.0rc1 experimental free-threading build (v3.13.0rc1:e4a3e786a5e, Jul 31 2024, 19:57:27) [Clang 15.0.0 (clang-1500.3.9.4)])
INFO: 40 tasks executed in 16.58s
```
5. free-threading build with GIL enabled
```
TODO
```

#### Test results on Windows
```
Windows 10, 64-bit  
CPUs = 8
```
1. multi-threads
```
python.exe -m hypercorn -w1 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 20:58:38) [MSC v.1940 64 bit (AMD64)])
INFO: 40 tasks executed in 31.31s
```
2. multiprocesses
```
python.exe -m hypercorn -w8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 20:58:38) [MSC v.1940 64 bit (AMD64)])
INFO: 40 tasks executed in 11.18s
```
3. subinterpreters
```
python.exe subinterpreter_web.py -w 8 flask_app:app
INFO: Testing server: (GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 20:58:38) [MSC v.1940 64 bit (AMD64)])
INFO: 40 tasks executed in 10.98s
```
4. free-threading
```
python.exe -Xgil=0 -m hypercorn -w1 flask_app:app
Cannot import flask! What now?
Test from `applications\desktop_app\main.py`:

python.exe -Xgil=0 applications\desktop_app\main.py
(GIL disabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 21:06:58) [MSC v.1940 64 bit (AMD64)])
40 tasks executed in 28.75843620300293 [s]
```
5. free-threading build with GIL enabled
```
python.exe -Xgil=1 applications\desktop_app\main.py
(GIL enabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Jul 31 2024, 21:06:58) [MSC v.1940 64 bit (AMD64)])
40 tasks executed in 77.3057336807251 [s]
```
