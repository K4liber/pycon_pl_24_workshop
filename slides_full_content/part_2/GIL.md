The Global Interpreter Lock, or GIL exist for thread-safety.

GIL is a mechanism used in the CPython interpreter to synchronize access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython's memory management is not thread-safe.  

The GIL was introduced as part of Python's threading implementation in 1992. Guido van Rossum, the creator of Python, chose to use a global lock for simplicity and speed. At the time, computers typically only had one CPU, so there was no real need for true thread-level parallelism. 

As multi-core processors became more common, the GIL became a bottleneck for multi-threaded Python programs. Even though multiple threads exist, the GIL allows only one of them to execute Python bytecodes at a time, which means that a single Python process cannot make use of multiple CPU cores.  

Over the years, there have been several attempts to remove or replace the GIL, but none have been successful. 
![alt text](../images/knights.png)
Removing the GIL entirely would require changes to CPython's memory management, which would likely slow down single-threaded programs. Replacing the GIL with finer-grained locks could also slow down the interpreter due to increased lock contention.  

Despite its limitations, the GIL makes it easier to write thread-safe Python code, since:
- you don't have to worry about simultaneous access to Python objects
- it also makes it easier to integrate with C libraries that are not thread-safe
- a lot of existing C extensions rely on GIL
- other garbage collection solutions may decrease the performance of single-threaded scripts
For these reasons, the GIL remains a fundamental part of CPython.

"Python uses a reference counter to support garbage collection and to free objects in the memory automatically when the counter reaches 0. In a single threaded environment, it works fine, but when you add support to threads, and support to share objects across thread, you need a thread-safe counter to prevent memory-leaks and prevent referencing dealocated addresses. The GIL is what makes all these counters thread-safe in a practical way, but has the disadvantage of making most multi-threaded code slow. Other languages (and even some Python interpreters) implement other garbage collection algorithms that do not require a GIL. CPython could adopt something in that direction, but there are 2 problems with that: (a) a lot of existing C extensions rely on GIL, and (b) other garbage collection solutions may decrease the performance of single-threaded scripts (which is not great already). Maybe after the faster cpython initiative, removing the GIL can become more feasible."  https://www.reddit.com/r/Python/comments/vgw40n/why_python_needs_the_gil_and_swift_doesnt/
