# GIL disabled

## Intro

The global interpreter lock has been holding Python back for years. That is about to change with Python 3.13.
But there are **dangers that you need to be aware of.**

The **aim of** the global interpreter lock, or **GIL** is to protect Python object access **by letting only one thread at a time to execute Python bytecode.**
With Python 3.13 GIL can be optional.
**Will it have any effect on you?**



## What is Python bytecode?

**Example of Bytecode**
Consider this simple Python function:


`def add(a, b):
    return a + b`
When compiled to bytecode, it might look something like this:


 2           0 LOAD_FAST                0 (a)
             2 LOAD_FAST                1 (b)
             4 BINARY_ADD
             6 RETURN_VALUE
Each line in the bytecode corresponds to an **operation** that the Python Virtual Machine will perform when running the function.

`LOAD_FAST` loads a local variable onto the stack.
`BINARY_ADD` pops the two topmost items from the stack, adds them, and pushes the result back onto the stack.
`RETURN_VALUE` pops the topmost item from the stack and returns it as the result of the function.


**Python bytecode** is an intermediate representation of your **Python code** that the **Python interpreter executes** (Cpython.exe). It’s generated by **compiling your source code** and is run by the Python Virtual Machine

## What is Python interpreter?
Software program that executes Python code:

1. Read (code) and Parse (for sytnax)
2. Compile to Bytecode
3. Execute Bytecode (by the Python interpreter's runtime environment)

**Types**
**1. CPython**: This is the reference implementation of Python, **written in C** and is the **default interpreter** you get when you download Python from python.org.

**2. PyPy** 
**3.IronPython**  An implementation of Python running on the .NET platform. 

## What is GIL
The GIL was introduced in Python 1.5.

**CPython**, the default Python interpreter,
has the GIL, currently in Python 3.12.

The Global Interpreter Lock (GIL) is a mutex (a type of lock) that protects access to Python objects. 


It ensures that only one thread can execute Python bytecode at a time in a single process, even on multi-core systems. This means that even if a program **has multiple threads, only one thread is executing Python code at any given moment.**


## Why the GIL Exisits is in Python

The GIL is primarily there to **simplify memory management**. 

Unfortunately it also means, you **can not effectviely use multiple CPU cores** in a multi-thereaded program.
For heavy computations, that **has an effect on performance.**



Python's **memory management, including garbage collection**, is **not thread-safe**, meaning that without the GIL, multiple threads could **modify objects in memory at the same time**, leading to corruption and crashes. The GIL prevents these issues by ensuring that only **one thread can execute Python bytecode at a time.**



**WHY DOES THE DEFAULT INTERPRETER HAVE THIS LOCK?**

 
In the early days, **mutli-threaded programs were less common than they are now**, and single-threaded performance was the main concern.

**Solution**:
Locking the interpreter (it is **in CPython using a bolean variable when executing a bytecode**) was a mechanism to improve execution time of single threaded code.

**Why?**
Mainly because that makes a (python) memory management much simpler. 

Python uses a combination of **reference counting** and a cyclic **garbage collector** to manage memory.
1. **Reference Count**: Every Python object maintains a count of the number of references pointing to it

2. **Cyclic Garbage collector**
**Circular References** reference counting fails to reclaim memory in the presence of **circular references** when two or more objects reference each other, creating a cycle.
**Cyclic Garbage Collector**: To handle such cases, Python’s garbage collector uses an algorithm to detect and **clean up these cycles**.


GIL makes it easier for developers to write safe **concurrent code**. Because of the protection against **race conditions** and **memory corruption**.

# Task processing and threading
## Performance increase without the GIL

Multithreaded, Multiprocessed explanation.

**Multiprocessed** is faster, it can now use multiple processes in order to handle all these different prime computations.


In `Python 3.12` difference between **single thereaded and multi-threaded is minimal**, because GIL is there, so you **can not benefit from multi-threaded** possibility.

 In `Python 3.13t` it is expected to be faster. 

Why do we even care about the **difference single threaded versus mutli-threaded if we have multi-processes**?

 

If you use **multit-processing module**,
You can indeed use **multiple CPU cores** because you are creating **separate processes**, but each of these processes is going to have its **own Python interpreter**.

 
And we can not really use multithreading here beacuse GIL prevent us from that.


## GIL is becoming optional
It has been requested for a long time. 

And it has been even more requested with the hype of AI 

Python community has been advocating for a solution to GIL limitations for years. 

 

There are already solutions for this like using libraries, **multiprocessing**, doing heavy calculations with **NumPy**, there are even other interpreters like **Jython** that already remove the GIL.

 

It will be really great if it will be **accesible for the base language and the most common interpreter, CPython.**

## The plan for GIL
## Potential issues with removing the GIL
## How much will this affect you?


# Questions
Q1: What is Python bytecode?
Q2: What is default Python interpreter? What it's name and what it does? 
Q3: What is GIL?
Q4: Why GIL exists?

# TASK 1
Analyze the code and run main with 
A. `python3.12`
B. `python3.13t` with GIL disabled
What are your conclusions for each mode (single-threaded, multi-threaded, multiprocessed)?


# TASK 2
In the function `multiprocess_count_primes` fix return value. 
Return value should be based on list of `multiprocessing.pool.ApplyResults` object. 

Hint: `sum([result.get() for result in results])`

Benchmark from ArjanCodes channel: https://www.youtube.com/watch?v=zWPe_CUR4yU
source: https://github.com/ArjanCodes/examples/blob/main/2024/gil/main.py
