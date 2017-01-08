from abc import ABCMeta, abstractmethod

class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        raise NotImplementedError('users must define foo to use this base class')

class Concret(Abstract):
    def foo(self):
        print('cat')

con = Concret()
con.foo()