class Test:
    x=20 #public (accesible anywhere)
    _y=10 #protected (can be accessed within same class ,subclass and even outside the class.)
    __z=30 #private (cannot be accessed directly outside the class.)
    def m1(self):
        print(self.x)
        print(self._y)
        print(self.__z)
obj=Test()
obj.m1()
print(Test.x)
print(Test._y)
print(Test.__z)

        