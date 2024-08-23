import gc

collected = gc.collect()
# Check for garbage-collected objects
print("Garbage objects:", collected)


class MyClass:
    def __init__(self):
        self.ref = None


# Create objects and a cycle
a = MyClass()
b = MyClass()
a.ref = b
b.ref = a

# Delete references to these objects
del a
del b

# Manually trigger garbage collection
unreachable_objects = gc.collect()

print(f"Unreachable objects collected: {unreachable_objects}")
