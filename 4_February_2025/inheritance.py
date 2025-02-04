class P:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        '''With the help of class mthod, memory utilisation and sharing is possible '''
        print("class method")
    @staticmethod
    def m3():
        '''Generic method , either use by class name or object name , no dependency'''
        print("static method")
class C(P):
    pass
c=C()
print(c.a)
c.m3()

'''Single Inheritance.'''
class person():
    def __init__(self, name, age, id):
        self.name=name
        self.age=age
        self.id=id
    def getinfo(self):
        return self.name,self.age,self.id
class emp(person):
    def __init__(self, name, age, id, sal):
        self.salary=sal
        super().__init__(name, age, id)
    def display(self):
        print(super().getinfo(),self.salary)
e=emp("ram",23,1234,98765)
e.display()


'''Multiple Inheritance problem.'''
class p1():
    '''Class P1'''
    def __init__(self):
        self.a=20
    def display(self):
        print("This is Class P1.", self.a)
class p2():
    '''Class P2'''
    def __init__(self):
        self.b=10
    def display(self):
        print("This is Class P2.", self.b)
class p3(p1,p2):
    '''Class P3'''
    '''Multiple Resolution Order.'''
    def __init__(self):
        p1.__init__(self)
        p2.__init__(self)
        #super().__init__()
    def display(self):
        p1.display(self)
        p2.display(self)
        #super().display()
obj=p3()
obj.display()
p3.mro()


'''Constructor Overloading'''
class Example():
    def __init__(self,a=None,b=None):
        self.a=a
        self.b=b
    def __str__(self):
        '''similar to .toString method in Java'''
        return str(self.a)
e1=Example()
e2=Example(99)
print(e2)