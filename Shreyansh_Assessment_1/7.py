'''Name = Shreyansh Srivastava'''
'''Questions = 1,4,7,8,10'''
'''Email Address = shreyanshsri19@gmail.com'''

class Employee(): # parent class
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

class Department(Employee): # child class 
    def __init__(self, name, id, dept):
        super().__init__(name, id, dept)
        self.dept=dept
        self.id=id

    def dsp(self):
        print("Department Details:")
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Dept : {self.dept}")


emp1=Department("Ram",101,"Tech") # object cretion for child class
emp2=Department("Shyam",102,"Finance") # object cretion for child class

emp1.dsp()
emp2.dsp()