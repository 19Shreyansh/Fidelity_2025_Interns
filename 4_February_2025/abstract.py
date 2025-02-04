'''Abstract Class Implementation.'''
'''Abstract class contains abstract methods and concrete methods(static and default methods)'''
'''If all methods are abstract , then it is an Interface.'''

from abc import *
'''abc is reserved keyword for abstract class'''
class example(ABC):
    @abstractmethod
    # @abstractmethod to implement abstract
    def m1(self):
        '''abstract method = no body'''
        pass
    def dsp(self):
        '''Not abstract method = concrete method = has a body'''
        print("Hello")
class a(example):
    def m1(self):
        print("m1 method is implemented in class a")
obj=a()
obj.m1()
obj.dsp()
