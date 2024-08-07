"""
The memory management mechanism in Python keeps track of object consumption by keeping track of the number of references to each object.
When an object’s reference count reaches zero, it is scheduled for removal.

This reference count technique isn’t thread-safe because Python was written at a time when multi-processor systems were uncommon and multi-core CPUs were non-existent.
Instead, Python achieves thread safety by allowing only one thread at a time to access an object. This is what the GIL is for.

https://medium.com/@essalhiwafaa05/python-is-removing-the-gil-and-increasing-concurrency-f38dcd6d4f5b

Unsafe manipulations of shared state and reference counts of shared objects can lead to memory leaks. There can be a case where reference count of an object will never reach 0 and python fails to free an allocated block of memory when no longer needed.
"""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import partial
import os
import sys
import threading


@dataclass(frozen=True)
class Person:
    name: str


@dataclass(frozen=True)
class Parent(Person):
    pass


@dataclass(frozen=True)
class Child(Person):
    parent: Parent

# _parent is a shared state
_parent = Parent(
    name='Alex'
)


def create_child(name: str, parent: Parent) -> Child:
    thread_id = threading.get_native_id()
    print(f'Creating a child, PID = {os.getpid()}, TID = {thread_id}')
    child = Child(
        name=name,
        parent=parent
    )
    print(f'Parent reference count: {sys.getrefcount(parent)}')
    return child


if __name__ == '__main__':
    tasks = []
    children_names = [
        'Bob',
        'Freddy',
        'Jackie',
        'Tito',
        'Jermaine',
        'Marlon',
        'Randy',
        'Janet',
        'Toya',
        'Rebbie',
        'Brandon',
        'Joh'
    ]
    number_of_workers = 8

    with ThreadPoolExecutor(number_of_workers) as executor:
        for name in children_names:
            task = executor.submit(partial(
                create_child,
                name=name,
                parent=_parent
            ))
            tasks.append(task)
        
    children = [task.result() for task in tasks]

    for child in children:
        print(f'Hello {child.name} {child.parent.name}!')
