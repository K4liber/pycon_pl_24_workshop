# Thread safety

### What is thread safe function?

- function that can be **safely** executed by multiple **threads concurrently** without causing unexpected results.


Key characterstics of thread-safe function are:

### No race conditions
A thread-safe function prevents race conditions, which occur when the **outcome** of a computation **depends** on the **timing** or **order** of execution of **multiple threads**.

### Proper synchronization
Mechanism like locks, etc to coordinate access to shared resources. (Queue)

### Immutability or Local state 
- **immutable** objects cannot be modified, multiple threads can safely access them concurrently
- **local variables** are inherently **thread-safe** because each thread has its own copy of the data

# GIL and thread safety 

GIL does not guarantee thread safety for all operations.

## Atomicity of operations

The GIL ensures that only one thread executes Python bytecode at a time for **atomic operations**.

## Releases of the GIL
If the function performs a sequence of operations like reading a value, modifying it, and then writing it back, this sequence is **not atomic**,  the GIL may be released, another **thread can interrupt** and modify the state between these operations

## Shared Mutable State
Since only **one thread can execute Python bytecode** at a time, it might seem safe, but if the GIL is released if the **task involves multiple steps** race conditions can still happen

## Timing Issues and Context Switching
Even with the GIL, the Python **interpreter can context switch between threads** at certain points. This can lead to situations where one thread partially completes an operation and is then preempted by another thread.

# Questions?

Q1. Is function below **atomic**?
`_global_dict[0] += 1`

A1. No, beacuse:
1. read the current value of `_global_dict[0]`
2. increments the value by 1
3. writes the incremented value back to `_global_dict[0]`


Q2. Is the function below **thread-safe**?
`def get_value(dictionary, key):`
    `return dictionary.get(key)`

A2. Yes, it is thread-safe because reading from a dictionary is an atomic operation in Python.

Q3. What is the race condition?

Ask someone to take a **C** ? 

Q4. Is **tuple** a **thread safe** object?
Yes, multiple threads can access them concurently, beacuse it is immutable. 


# Task 2
Analyze `test` with `no_thread_safe_task` and implement similar test that uses `illusional_thread_safe_task` and `indeed_thread_safe_task`.
Evaluate it by running `pytest` in terminal and configured `testing addin`.