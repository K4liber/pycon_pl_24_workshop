### Running on windows

If python fails to fing QT plugins, please set the QT_PLUGIN_PATH environment variable:  
```
cmd /C "set QT_PLUGIN_PATH=<absolute_path_to_venv>\Library\plugins\platforms && python main_qt.py"
```

### Run the application

With GUI:  
`python main_qt.py`  

or as a script (you can change the runner type by modifying `runner_type` variable in `applications/desktop_app/main.py`):  

`python main.py`  

please use `-Xgil=0` flag to force free-threaded Python running with GIL disabled:  

`python -Xgil=0 main.py`

### Test LINUX

Linux 5.15.0-58-generic #64~20.04.1-Ubuntu x86_64 x86_64 x86_64 GNU/Linux  
CPUs = 2

```
(THREAD)
(GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
All tasks completed successfully in 110.24 [s]. Init time: 0.54 [s].
PID to memory usage (in MB): {6276: 83.1796875}
Overall memory usage: 83.1796875 [MB]

(PROCESS)
(GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
All tasks completed successfully in 41.74 [s]. Init time: 0.17 [s].
PID to memory usage (in MB): {6869: 84.25390625, 6917: 37.51171875, 6914: 37.43359375, 6912: 37.6875, 6915: 37.51171875, 6909: 37.7734375, 6916: 37.48828125, 6918: 37.6484375, 6913: 37.51953125}
Overall memory usage: 384.828125 [MB]

(SUBINTERPRETER)
(GIL enabled) 3.13.0rc1 (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 10:36:31) [GCC 9.4.0])
All tasks completed successfully in 41.62 [s]. Init time: 1.37 [s].
PID to memory usage (in MB): {7337: 81.73828125}
Overall memory usage: 81.73828125 [MB]

(FREE-THREADING)
(GIL disabled) 3.13.0rc1 experimental free-threading build (tags/v3.13.0rc1:e4a3e78, Aug 24 2024, 09:52:40) [GCC 9.4.0])
Run time [s]: 76.999347448349
