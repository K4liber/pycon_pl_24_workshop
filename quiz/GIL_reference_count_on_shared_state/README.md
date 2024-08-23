# Memory management
The memory management mechanism in Python keeps track of object consumption by keeping track of the number of references to each object.
When an object’s reference count reaches zero, it is **scheduled for removal**.

## Reference count 
This reference count technique **isn’t thread-safe** because Python was written at a time 
when multi-processor systems were uncommon and multi-core CPUs were non-existent.
Instead, **Python achieves thread safety by allowing only one thread at a time** to access an object. 
This is what the GIL is for.

https://medium.com/@essalhiwafaa05/python-is-removing-the-gil-and-increasing-concurrency-f38dcd6d4f5b

Unsafe manipulations of shared state and **reference counts of shared objects can lead to memory leaks**. 
There can be a case where **reference count of an object will never reach 0 and python fails to free** 
an allocated block of memory when no longer needed.


# TASK 1
Why function `sys.getrefcount` always include 2 references more than the actual references we can get from function `gc.get_referrers`?

In summary, the primary difference comes from the fact that `sys.getrefcount` includes temporary references created during its own call, whereas `gc.get_referrers` does not.
`sys.getrefcount(obj)`
- includes all references to the object, including temporary references created by the function call itself.
- The act of passing obj to `sys.getrefcount()`creates temporary reference to the passed object and it increments the reference count by 1
# TASK 2
import gc library and check how many references are collected
Check using garbage collector `gc.collect()`?

# TSAK 3s
How many reference counts will have `parent` after creating 12 `childrens`?

