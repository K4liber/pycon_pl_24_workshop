# GIL disabled

## Intro

The global interpreter lock has been holding Python back for years. That is about to change with Python 3.13.
But there are **dangers that you need to be aware of.**

The **aim of** the global interpreter lock, or **GIL** is to protect Python object access **by letting only one thread at a time to execute Python bytecode.**
With Python 3.13 GIL can be optional.
**Will it have any effect on you?**

## What is Python bbytecode?

**Example of Bytecode**
Consider this simple Python function:


`def add(a, b):
    return a + b`
When compiled to bytecode, it might look something like this:

css
Skopiuj kod
 2           0 LOAD_FAST                0 (a)
             2 LOAD_FAST                1 (b)
             4 BINARY_ADD
             6 RETURN_VALUE
Each line in the bytecode corresponds to an operation that the Python Virtual Machine will perform when running the function.

LOAD_FAST loads a local variable onto the stack.
BINARY_ADD pops the two topmost items from the stack, adds them, and pushes the result back onto the stack.
RETURN_VALUE pops the topmost item from the stack and returns it as the result of the function.


## What is GIL


2:12 Why the GIL is in Python

2:52 Performance increase without the GIL

4:53 GIL is becoming optional

5:34 The plan for GIL

6:44 Potential issues with removing the GIL

8:31 How much will this affect you?

9:45 Outro


Q1: What is Python bytecode?
