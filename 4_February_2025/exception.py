 #exception=unwanted , unexpeted event that will block program abnormaly'''

''' always prefer specific exception instead of generic exception '''

# try:
#     x=int(input("Enter a number : "))
#     y=int(input("Enter another number : "))
#     print(x/y)
# except Exception as msg:
#     print(msg.with_traceback)
# except ArithmeticError as msg:
#     print(msg)

# except ZeroDivisionError:
#     print("Invalid input")
# except ValueError:
#     print("Value Error")

# '''Creating your own Exception.'''
# class TooyoungException(Exception):
#     def __init__(self, msg):
#         self.msg=msg

# age=10
# if age<=18:
#     raise TooyoungException("Under Aged .")

class InvalidID(Exception):
    def __init__(self, msg):
        self.msg=msg
class Employee:
    def __init__(self, name, dep, id):
        self.name = name
        self.dep = dep
        if not id.isdigit():
            raise InvalidID("Enter only numbers in ID")
        if len(id) < 4:
            raise InvalidID("ID has to be 4 or more digits long")
        self.id = int(id)
    def display(self):
        print(f"Name: {self.name}, Department: {self.dep}, ID: {self.id}")
a=Employee("FIL","ISS","1202")
a.display()

