'''Has-A Relationship.'''
class engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print(self.a)
class car:
    def __init__(self):
        self.engine =engine()
    def m2(self):
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c=car()
c.m2()

'''Composition'''
class car:
    def __init__(self,name,model,colour):
        self.name=name
        self.model=model
        self.colour=colour
    def display(self):
        print("Details of the car are :")
        print("Name of the car :",self.name)
        print("Model of the car :",self.model)
        print("Colour of the car :",self.colour)
class employee:
    def __init__(self,name,id,car):
        self.name=name
        self.id=id
        self.car=car
    def display(self):
        print("Name of the Employee : ",self.name)
        print("ID of the Employee : ",self.id)
        self.car.display()
c=car("Keoningsegg","Jesko","Black")
e=employee("Ram","A11111",c)
e.display()


class address():
    def __init__(self,house_no,sector,city,state):
        self.house_no=house_no
        self.sector=sector
        self.city=city
        self.state=state
    def display(self):
        print("Address of the employee is : ")
        print("House No. : ",self.house_no)
        print("Sector : ",self.sector)
        print("City : ",self.city)
        print("State : ",self.state)
class employee():
    def __init__(self,name,id,addr):
        self.name=name
        self.id=id
        self.addr=addr
    def display(self):
        print("Name of the employee is :",self.name)
        print("Id of the employee is :",self.id)
        self.addr.display()
a=address("307","Sector 48","Gurugram","Harayana")
e=employee("Ram","A1234",a)
e.display()
