'''OOPS Concepts !'''

class Student:
    def __init__(self):
        '''Default constructor'''
        self.name ="Steve"
        self.age=40
        '''Two instance variables here.'''
    def dsp(self):
        print(self.name,self.age)
s=Student() 
'''Creating an object of class Student.'''
s.dsp()

class Student:
    def __init__(self,name,age):
        '''Parameterised constructor'''
        self.name =name
        self.age=age
        '''Two instance variables here.'''
    def dsp(self):
        print(self.name,self.age)
s=Student("Rahul",47) 
'''Creating an object of class Student.'''
s.dsp()

class Student:
    __a=10
    def dsp(self):
        print(self.a)
    @classmethod
    def m1(cls):
        print(cls.a)
s=Student()
Student.m1()

