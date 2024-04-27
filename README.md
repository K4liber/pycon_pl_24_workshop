# PyCon PL'24 

## Tytuł zgłoszenia:
 
Multicore processing in Python with Per-interpreter GIL

## Krótki opis(128)
 
Exploring a new feature in Python called Per-interpreter GIL. It allows using multiple cores in a single Python process.

## Cel propozycji (3072)
 
`Napisz krótko co jest celem Twojej propozycji (np. zapoznanie uczestników z ciekawym problemem X, biblioteką Y, którą stworzyłeś/stworzyłaś)`

Per-interpreter GIL aims to utilize computing resources in a more efficient way. The feature is accessible through the Python/C API starting from Python version 3.12. A Pythonic interface for this feature is anticipated to be released with Python version 3.13 (coming out on October 2024).

During the workshop we are going to learn:

- Threads vs. Processes in Python: Participants learn about threads, processes, and the Global Interpreter Lock (GIL). Threads are lightweight units within a process, while processes are independent units with their memory space. The GIL ensures thread safety but limits multi-core usage.

- Python Interpreter and GIL: The workshop explains Python's interpreter and the purpose of the GIL. Although it slows down multi-threaded programs, it ensures thread safety and facilitates I/O operations.

- Challenges with Disabling the GIL: Disabling the GIL for running pure Python functions across threads is risky due to implicit actions by the interpreter. While the GIL can limit the execution speed of multi-threaded Python programs, it greatly simplifies development.

- Introducing Per-interpreter GIL: Python 3.12 introduces the Per-interpreter GIL, addressing the limitations of the traditional GIL. It promises better multi-core utilization and performance improvements.

- Real-life Applications: The workshop discusses practical applications of the Per-interpreter GIL, such as server-side processing. It optimizes performance by reducing overhead when handling complex requests.

- Performance Benchmarks: Attendees explore performance benchmarks comparing thread-based, process-based, and Per-interpreter GIL-based execution. The Per-interpreter GIL architecture shows potential performance gains.

- Key Takeaways: Participants learn about the role of Python Enhancement Proposals (PEPs) and the trade-offs of the GIL. Despite its limitations, Python remains popular due to its simplicity and flexibility.

- Hands-On Experience: Participants engage in hands-on activities using a QT-based GUI application to demonstrate multi-core execution. They also explore alternatives like JavaScript Web Workers and C# Task Parallel Library (TPL) for comparison.

In summary, the workshop equips participants with a better understanding of Per-interpreter GIL and its benefits for multi-core processing in Python.

## Grupa docelowa (3072)
 
`Napisz krótko, do kogo adresowana jest Twoja propozycja (np. osoby tworzące aplikacje webowe)`

TODO
 
## Szczegółowy abstract (6144)
 
`Zamieść szczegółowy opis swojej propozycji (opis ten będzie widoczny dla Komitetu Programowego, natomiast nie będzie publicznie dostępny na stronie w razie akceptacji)`

TODO
 
## Plan propozycji (3072)

`Przedstaw plan swojej propozycji w punktach, przypisując ilość czasu na poszczególne jej części`

TODO
 
## Uwagi
