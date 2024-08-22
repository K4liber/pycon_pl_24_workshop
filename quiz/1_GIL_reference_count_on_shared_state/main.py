from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import partial
import gc
import os
import sys
import threading
from typing import Any


@dataclass(frozen=True)
class Person:
    "I am only human after all."
    name: str


@dataclass(frozen=True)
class Parent(Person):
    "I am a parent to my growth and happines."


@dataclass(frozen=True)
class Child(Person):
    "I allow myself to nourish my inner child."
    parent: Parent

# _parent is a shared state
_parent = Parent(
    name='YOUCAN'
)


def print_reference_count(obj: Any) -> None:
    "How many people refer to one person?"
    print(f'{str(obj)} reference count: {sys.getrefcount(obj)}')

def print_reference_count_gc(obj: Any) -> None:
    "How many people refer to one person?"
    print(f'{str(obj)} reference count: {len(gc.get_referrers(obj))}')


def print_references(obj: Any) -> None:
    "Who are are the people that reference to a given person?"
    for ref_index, ref in enumerate(gc.get_referrers(obj), start=1):
        if isinstance(ref, dict) and '__name__' in ref:
            ref_name = ref['__name__']
        else:
            ref_name = str(ref)

        print(f'Ref {ref_index}: {ref_name}')


def print_reference_summary(obj: Any) -> None:
    "How many people and who are they who reference to one person?"
    print("----- Reference summary started -----")
    print_reference_count_gc(obj=obj)
    print('\nReferences:\n')
    print_references(obj=obj)
    print("------ Reference summary ended -----")


def create_child(child_name: str, parent: Parent) -> Child:
    "Go for your dream!"
    thread_id = threading.get_native_id()
    print(f'Creating a child, PID = {os.getpid()}, TID = {thread_id}')
    child = Child(
        name=child_name,
        parent=parent
    )
    print_reference_count_gc(parent)
    return child


if __name__ == '__main__':
    print("\n----- INITIAL STATE -----\n")
    print("\n----- Reference summary started -----\n")
    print_reference_count(obj=_parent)
    print('\nReferences:\n')
    print_references(obj=_parent)
    print("\n------ Reference summary ended -----\n")
    tasks = []
    children_names = [
        'Joy',
        'Freedom',
        'Passion',
        'Dedication',
        'Hope',
        'Garden',
        'Sport',
        'Complexity',
        'Growth',
        'Intgration',
        'Harmony',
        'Strategy'
    ]
    NO_OF_WORKERS = 8

    with ThreadPoolExecutor(NO_OF_WORKERS) as executor:
        for child_name in children_names:
            task = executor.submit(partial(
                create_child,
                child_name=child_name,
                parent=_parent
            ))
            tasks.append(task)
        
    children = [task.result() for task in tasks]

    for child in children:
        print(f'Hello {child.name} {child.parent.name}!')
    print("\n----- FINDING PURPOSE STATE -----\n")
    print("\n----- Reference summary started -----\n")
    print_reference_count_gc(obj=_parent)
    print('\nReferences:\n')
    print_references(obj=_parent)
    print("\n------ Reference summary ended -----\n")
