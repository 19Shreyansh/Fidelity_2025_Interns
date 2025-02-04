# '''exception=unwanted , unexpeted event that will block program abnormaly'''
# ''' always prefer specific exception instead of generic exception '''
# # try:
# #     x=int(input("Enter a number : "))
# #     y=int(input("Enter another number : "))
# #     print(x/y)
# # # except Exception as msg:
# # #     print(msg.with_traceback)
# # except ArithmeticError as msg:
# #     print(msg)

# # except ZeroDivisionError:
# #     print("Invalid input")
# # except ValueError:
# #     print("Value Error")

# # '''Creating your own Exception.'''
# # class TooyoungException(Exception):
# #     def __init__(self, msg):
# #         self.msg=msg

# # age=10
# # if age<=18:
# #     raise TooyoungException("Under Aged .")

# class empexcept(Exception):
#      def __init__(self, msg):
#           super.__init__(msg)
#           #self.msg=msg
# class employee():
#     def __init__(self,name,role,id):
#         self.name = name
#         self.role = role
#         self.id = id
#         if not id.isdigit():
#              raise empexcept("Please enter digits only.")
#         if len(self.id) < 4:
#              raise empexcept("Please enter digits of minimum length 4")
#         def display(self):
#             print(f"Name : {self.name} role : {self.role} id : {self.id}")
        
# try:
#     e=employee("Rahul","SDE","A1234")
#     e.display()
# except empexcept as ee:
#         print(e.msg)
# try:
#     e=employee("Rahul","SDE","01234")
#     e.display()
# except empexcept as ee:
#         print(e.msg)
# try:
#     e=employee("Rahul","SDE","1234")
#     e.display()
# except empexcept as ee:
#         print(e.msg)

