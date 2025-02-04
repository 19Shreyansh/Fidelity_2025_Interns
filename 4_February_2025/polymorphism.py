'''Polymorphism'''
class P:
    '''Parent Class'''
    def __init__(self):
        self.a=0
    def m1(self):
        print("Parent Class")
class C(P):
    '''Child Class'''
    def __init__(self):
        self.b=0
    def m2(self):
        print("Child Class")
c=C()
c.m1()
c.m2()

