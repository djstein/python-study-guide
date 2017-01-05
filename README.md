#Study Guide
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
Used for pretty much everything, ordered, any type of object
```python
list = [1, 2, 3]
list.insert(x)

#CAN ONLY USE .sort() ON LISTS

list.sort()
```

### Array
In Python, is small wrapper for C array (typically not used)

Represent basic values, chars, ints, floats, unicode. Corresponding varients for signed / unsigned
```python
from array import array

x = array('l', [1,2,6,8])
x.append(4)
>>> array('l', [1, 2, 6, 8, 4])
```

### Tuple
Values separated by a comma, values inside are **immutable**
```python
tuple = ‘hello’, 123, ‘world’
```

### Set
Unordered with no duplicates

```python
set = {‘apple’, ‘orange’, ‘apple’, ‘pear’}
print(set)
>>> {‘apple’, ‘orange’, ‘pear’}
```

Can do relational algebra set operations on
```python
a = set(‘abracadabra’) 
b = set(‘alacazm’)
a - b
>>> {‘r’, ‘d’, ‘b’}   etc etc
```

### Dictionary 
Dictionaries in Python are key: value pairs, unordered, implemented by a hashtable but used like hashmap

```python
tel = {‘jack’: 4098, ‘sape’: 4139}
tel[‘guido’] = 4127
>>> {‘sape’: 4139, ‘guido’:4127, ‘jack’: 4098}

# or use constructor
dict( [  (’sape’, 4139), (‘guido’, 4127), (‘jack’, 4098) ] )
```

### Sorting Data Structures
List uses .sort() to sort data for that instance

All other iterable data structures use sorted(), which returns a new sorted instance

Sort and sorted call timsort at C level, average complexity of **O(n log n)**

## Classes and Inheritance

Advanced example showing:

```python
class Dog():
    kind = 'canine'    # class variable shared by all instances

    # init must take argument if given
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []

    def tricks(self):
        self.tricks.append('sit')


class BigDog(Dog):

    def tricks(self):
        self.tricks.append('eat turkey')

d = Dog('Fido')
e = Dog('Buddy')
d.kind
>>> 'canine'
e.name
>>> 'Buddy'
```

## Star and Double Star: Usage of * and ** for Passing Arbitrary Number of Arguments
This is used for passing arbitray number of arguments to a function.
In strict type coding languages this is typically seen as overloading, where multiple function definitions have the same name but variable arguments.
```java
class DisplayOverloading
{
    public void disp(char c)
    {
         System.out.println(c);
    }
    public void disp(char c, int num)
    {
         System.out.println(c + " "+num);
    }
}
class Sample
{
   public static void main(String args[])
   {
       DisplayOverloading obj = new DisplayOverloading();
       obj.disp('a');
       obj.disp('a',10);
   }
}
```
However in Python this is atypical to use, and instead use variable amount of arguments via *args or **kwargs.

\*: pass arbitrary number of arguments

\**: pass arbitrary number of dict values 

```python
def func(*args)
    . . .

def func(*args, **kwargs)
    . . .

# — or --
def func(x, y, z)
    . . .

list = [1,2,3]
function(*list)

dict = [‘x’:1, ‘y’:2, ‘z’:3]
function(**dict)
```

## Decorators
What are decorators?

## Test Driven Development
Where tests are added prior to creation of new feature. The new test contains expected behavior of the feature to be added and should not pass until implementation of feature is correct. Ensures developers are not writingt tests bases on output of development and ensures test cases are already written, speeding up development time / addition of features later.

White Box: tester knows implementation

Black Box: tester does not know implementation

For Python use the unittest
```python
# Basic Example

import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    def tearDown(self):
        self.widget.dispose()
```

## Multithreading

## General Topics

### BFS

### DFS

### Hash Table

### Hash Map

### Enums

### Abstract Classes
A class that contains abstract methods, methods that are declared but contain no implementations. Use as structures for what methods a subclass should contain.
While typically not implemented in Python, useage of standard inheritance is prefered, they can be using the Python abc modul (Abstract Base Classes: https://docs.python.org/3/library/abc.html)

```python
from abc import ABCMeta

class Abstract(metaclass=ABCMeta):
    def foo():
        pass

class Concret(Abstract):
    def foo(self):
        print('cat')

con = Concret()
con.foo()
>>> 'cat'
```
