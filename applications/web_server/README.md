Exercise based on subinterpreter web server implementation by Anthony Shaw
(https://github.com/tonybaloney/subinterpreter-web)

`Python 3.13.0b3 experimental free-threading build (heads/3.13.0b3:7b413952e8, Aug  3 2024, 14:47:48) [GCC 9.4.0] on linux`

Step 1. Turn on webserver.

1. multi-threads:
```
python -m hypercorn -w1 flask_app:app
```
2. multiprocesses
```
python -m hypercorn -w8 flask_app:app
```
3. subinterpreters
```
python subinterpreter_web.py -w 8 flask_app:app
```
4. free-threading
```
python -Xgil=0 -m hypercorn -w1 flask_app:app
```

Step 2. Test sending multiple requests to the web-server under one case scenario
(multi-threads, multiprocesses, subinterpreters, free-threading )

```
python test_web_server.py
```
