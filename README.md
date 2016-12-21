# Python Study Guide
Python Study Guide

## Python Memory Management:
Use of private heap containing all Python objects and data structures.  User has no control, done by interpreter.
Raw memory allocator: Ensure enough memory from OS
Most work done by object-specific allocators. Objects are all treated differently, due to each needing storage requirements and space/speed tradeoffs
Heap space is allocated by Python/C API

## Python Garbage Collection:
Python object have reference count, count of objects pointing to it. when reference count is zero object is freed. Make use of reference cycles to find all objects that are unreachable. Unreachable objects include container objects: lists, dicts, instances, classes, tuples. Ints / Strings are not containers. Knows about each of these and c

## Python Data Structures
### List
used for pretty much everything, ordered, any type of object

list = [1, 2, 3]
list.insert(x)
CAN ONLY USE .sort() on lists.
list.sort()

### Array
in Python is small wrapper for C array (will not use)

### Tuple
values separated by a comma, values inside are immutable
tuple = ‘hello’, 123, ‘world’

### Set
unordered with no duplicates

set = {‘apple’, ‘orange’, ‘apple’, ‘pear’}
print(set) —> {‘apple’, ‘orange’, ‘pear’}
can do relational algebra set operations on
a = set(‘abracadabra’) 
b = set(‘alacazm’)
a - b -> {‘r’, ‘d’, ‘b’}   etc etc

### Dictionary 
key: value pairs, unordered, implemented by a hashtable but used like hashmap
tel = {‘jack’: 4098, ‘sape’: 4139}
tel[‘guido’] = 4127
tel —> {‘sape’: 4139, ‘guido’:4127, ‘jack’: 4098}
or use constructor
dict( [  (’sape’, 4139), (‘guido’, 4127), (‘jack’, 4098) ] )


ALL OTHER ITERABLE DATA STRUCTURES USE function sorted()
BOTH call timsort at the C level, has complexity of O(n log n)
Usage of * and ** for Passing Arbitrary Number of Arguments
*: pass arbitrary number of arguments
**: pass arbitrary number of dict values 
def func(*args)

def func(*args, **kwargs)

— or --
def func(x, y, z)
 …
list = [1,2,3]
function(*list)
dict = [‘x’:1, ‘y’:2, ‘z’:3]
function(**dict)