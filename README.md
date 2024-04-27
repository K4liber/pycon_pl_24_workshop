# PyCon PL'24 

## Tytuł zgłoszenia:
 
Multicore processing in Python with Per-interpreter GIL

## Krótki opis(128)
 
Exploring a new feature in Python called Per-interpreter GIL. It allows using multiple cores in a single Python process.

## Cel propozycji (3072)
 
`Napisz krótko co jest celem Twojej propozycji (np. zapoznanie uczestników z ciekawym problemem X, biblioteką Y, którą stworzyłeś/stworzyłaś)`

We are going to take a closer look at a new feature in Python called Per-interpreter GIL. The workshop equips participants with a better understanding of Per-interpreter GIL and its benefits for multi-core processing in Python. It aims to utilize computing resources in a more efficient way. The feature is accessible through the Python/C API starting from Python version 3.12. A Pythonic interface for this feature is anticipated to be released with Python version 3.13 (coming out on October 2024).

During the workshop we are going to learn:

- Threads vs. Processes in Python: A reminder and summary of threads, processes, and the Global Interpreter Lock (GIL). We are going to explain how do we use threads and processes in Python and why GIL has such a poor reputation.

- Python Interpreter and GIL: The workshop explains Python's interpreter and the advantages of the GIL. Although the GIL slows down multi-threaded programs, it ensures thread safety and facilitates I/O operations. It can limit the execution speed of multi-threaded Python programs, but greatly simplifies development.

- Challenges with Disabling the GIL: Disabling the GIL for running pure Python functions across threads is risky due to implicit actions by the interpreter. We are going to provide example scenarios and test them together.

- Introducing Per-interpreter GIL: Python 3.12 introduces the Per-interpreter GIL, addressing the limitations of the traditional GIL. It promises better multi-core utilization and performance improvements.

- Real-life Applications: The workshop discusses practical applications of the Per-interpreter GIL, including processing within desktop application and server-side processing.

- Hands-On Experience: Participants engage in hands-on activities using a QT-based GUI application and Python based server to test different multi-core processing scenarios. We are going to test how much the new feature optimizes performance by reducing overhead when handling complex requests.

- Performance Benchmarks: Attendees explore performance benchmarks comparing thread-based, process-based, and Per-interpreter GIL-based execution. We are going to visualize results of the benchmarks and judge if Per-interpreter GIL architecture shows significant performance gains in the long term perspective.

## Grupa docelowa (3072)
 
`Napisz krótko, do kogo adresowana jest Twoja propozycja (np. osoby tworzące aplikacje webowe)`

The workshop is addressed to people who use concurrent programming or parallel programming when creating applications ...

## Szczegółowy abstract (6144)
 
`Zamieść szczegółowy opis swojej propozycji (opis ten będzie widoczny dla Komitetu Programowego, natomiast nie będzie publicznie dostępny na stronie w razie akceptacji)`

TODO
 
## Plan propozycji (3072)

`Przedstaw plan swojej propozycji w punktach, przypisując ilość czasu na poszczególne jej części`

1. Theoretical part (30 minutes)

TODO

2. Practical part (60 minutes)

- Installing the required python environemnt.
- Exercise 1. Undestanding the GIL importance.
- Exercise 2. Testing Per-Interpreter GIL performance for a server-side programming.
- Exercise 3. Testing Per-Interpreter GIL performance for desktop (PyQT) applications.
- Exercise 4. Visualization of performance benchmarks results.

TODO

## Uwagi
