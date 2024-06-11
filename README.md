# PyCon PL'24 

## Tytuł zgłoszenia:
 
Multi-core processing in Python using Per-interpreter GIL

## Krótki opis(128)
 
Exploring a new Python feature called Per-interpreter GIL. It allows to use multiple cores in a single Python (CPython) process.

## Cel propozycji (3072)
 
`Napisz krótko co jest celem Twojej propozycji (np. zapoznanie uczestników z ciekawym problemem X, biblioteką Y, którą stworzyłeś/stworzyłaś)`

We are going to take a closer look at a new feature in Python (CPython) called Per-interpreter GIL. The workshop equips participants with a better understanding of Per-interpreter GIL and its benefits for multi-core processing in Python. It aims to utilize computing resources in a more efficient way. The feature is accessible through the Python/C API starting from Python version 3.12. A Pythonic interface for this feature is anticipated to be released with Python version 3.13 (coming out on October 2024).

During the workshop we are going to learn:

- Threads vs. Processes in Python: A reminder and summary of threads, processes, and the GIL (Global Interpreter Lock). We are going to explain how do we use threads and processes in Python and why GIL has such a poor reputation.

- Python Interpreter and GIL: The workshop explains Python's interpreter basics and the advantages of the GIL. Although the GIL slows down multi-threaded programs, it ensures thread safety and facilitates I/O operations. It can limit the execution speed of multi-threaded Python programs, but greatly simplifies development.

- Challenges with Disabling the GIL: Disabling the GIL for running pure Python functions across threads is risky due to implicit actions by the interpreter. We are going to provide example scenarios and test them together.

- Introducing Per-interpreter GIL: Python 3.12 introduces the Per-interpreter GIL, addressing the limitations of the traditional GIL. It promises better multi-core utilization and performance improvements.

- Real-life Applications: The workshop discusses practical applications of the Per-interpreter GIL, including processing within desktop application and server-side processing.

- Hands-On Experience: Participants engage in hands-on activities using a QT-based GUI application and Python based server to test different multi-core processing scenarios. We are going to test how much the new feature optimizes performance by reducing overhead when handling complex requests.

- Performance Benchmarks: Attendees explore performance benchmarks comparing thread-based, process-based, and Per-interpreter GIL-based execution. We are going to visualize results of the benchmarks and judge if Per-interpreter GIL architecture shows significant performance gains in the long term perspective.

## Grupa docelowa (3072)

`Napisz krótko, do kogo adresowana jest Twoja propozycja (np. osoby tworzące aplikacje webowe)`

The workshop is addressed to intermediate programmers:

If you use concurrent programming or parallel programming when creating applications, the workshop will suit you well. We are going to remind how one can use concurrent and parallel programming in Python. There is no need to already have an advanced knowledge on those topics. Since a significant amount of Python programs use some form of demanding calculations, it is valuable to know all the available options when it comes to parallel programming. If you eager to optimize your computations in Python, the workshop could help you with that.

Note for Python newbies/beginners:

While the workshop is targeted towards intermediate programmers, beginners with basic IT knowledge are also welcome to attend and can benefit from the workshop. Being a PyCon participant does not always indicate any knowledge about Python. For example, one might be a Java programmer and out of curiosity would like to see what's going on on the other side of the force. Without any Python knowledge, the workshop can still be a valuable experience, beacuse we are going to present some generic IT concepts. Every person with basic IT knowledge can learn something from the workshop. If you just starting with Python, it could be hard to understand some of the things we are going to talk about. Still you will manage to understand some parts and can ask for clarification on the other ones. We are happy to answer your questions both during the workshop and after its completion.

## Szczegółowy abstract (6144)
 
`Zamieść szczegółowy opis swojej propozycji (opis ten będzie widoczny dla Komitetu Programowego, natomiast nie będzie publicznie dostępny na stronie w razie akceptacji)`

1. About

The workshop focuses on a practical exploration of a relatively new feature in Python known as the Per-interpreter GIL. The Per-interpreter GIL enables multiple cores utilization within a single Python process. This feature is accessible through the Python/C API starting from Python version 3.12. A Pythonic interface for this feature is anticipated to be released with Python version 3.13 (coming out on October 2024).

2. Using Threads and processes in Python

Threads and processes are two fundamental units of program execution. While both are integral to how a computer performs tasks, they possess distinct characteristics and fulfill different purposes. Threads are lightweight units of execution that share the same memory space within a single process, allowing for efficient tasks concurrency. Processes are independent units of execution, each with its own memory space, providing strong isolation but requiring more resources and complexity to communicate between them. Understanding how one can utilize advantages of threads and/or processes in Python can help to execute computations more optimally.

3. Combating the disadvantages of GIL

The GIL assure that only one thread executes Python bytecode at a time. While the GIL can limit the execution speed of multi-threaded Python programs, it greatly simplifies development. For instance, performing operations on a shared dictionary across multiple threads will not lead to race conditions or data corruption. Furthermore, the GIL is released during I/O operations, such as reading or writing to a file or socket, which allows threads to run in parallel in these scenarios. The GIL is designed to facilitate multi-threading, and understanding its behavior can help developers write more efficient code. Disabling the GIL to execute a set of pure Python functions across multiple threads might seem safe, especially if those functions do not appear to manipulate the shared state explicitly. However, the CPython interpreter performs certain implicit actions that may affect the shared state. For example, operations altering "reference counts" and "string interning" are two mechanisms utilizing the shared state. Because of that, it is not safe to disable the GIL for "pure" Python functions in multi-threaded execution. Even if functions appear pure at the code level, they may not be pure in the context of the CPython interpreter, which involves the shared state access during execution. Another strategy to bypass GIL is to use a Python implementation without GIL, such as PyPy, Jython, or IronPython. Obviously, not a lot of us are eager to do it. CPython is the reference implementation of the Python programming language and effectively attracts developers with a wealth of useful libraries. With the Per-interpreter GIL we get following advantages:
- multi-core utilization in a single python process (no need for spawning processes which can introduce considerable communication and memory overhead)
- still using reference Python implementation (CPython) with a wealth of useful libraries
- simplified development due to the GIL

4. Benchmark summary

Beyond theoretical explanation, we are going to present a performance of regular threads/processed based applications in comparison to Per-interpreter GIL based one. We are going to prepare a basic sever-side and desktop (PyQT) applications to experiment with. The participants are going to play with the prepared code. We will together experiment with different scenarios. As a final step, together, we are going to discuss and summarize the benefits we can get from using the Per-interpreter GIL.

## Plan propozycji (3072)

`Przedstaw plan swojej propozycji w punktach, przypisując ilość czasu na poszczególne jej części`

1. Theoretical part (30 minutes)

- Threads and processes in Python
- Historical background of GIL existence
- Combating the disadvantages of the existence of GIL
- Overview on "PEP 684 – A Per-Interpreter GIL"
- Overview on "PEP 554 – Multiple Interpreters in the Stdlib"

2. Practical part (60 minutes)

- Installing the environemnt.
- Exercise 1. Undestanding the GIL importance.
- Exercise 2. Testing Per-Interpreter GIL performance for a server-side programming.
- Exercise 3. Testing Per-Interpreter GIL performance for desktop (PyQT) applications.
- Exercise 4. Creating a summary of performance benchmarks results (e.g. in form of a chart).

## Uwagi
Go to links.md.