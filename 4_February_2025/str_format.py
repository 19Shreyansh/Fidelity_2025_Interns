class Student:
    '''__str__ is being used here. with different place holders.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        '''0 and 1 here are Place Holders.'''
        msg=f'name is {self.name} and age is {self.age}'
        return msg
        #return ("name is {0} and age is {1}".format(self.name,self.age))
s=Student("Rahul",23)
print(s.__str__())
print(s)
