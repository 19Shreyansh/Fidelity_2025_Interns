'''Name = Shreyansh Srivastava'''
'''Questions = 1,4,7,8,10'''
'''Email Address = shreyanshsri19@gmail.com'''

from abc import *

class bank(ABC): # global class
    def bank_info(self):
        print("Welcome to Bank")
    @abstractmethod
    def interest(self): # abstract class
        pass

class hdfc(bank): # concrete class
    def interest(self):
        print("Interest Rate of HDFC is 7%")

class sbi(bank): # concrete class
    def interest(self):
        print("Interest Rate of SBI is 5%")

HDFC=hdfc() #object creation for hdfc
SBI=sbi() #object creation for sbi 

HDFC.bank_info() # calling the global class function for the object
HDFC.interest() # calling the global class function for the object

SBI.bank_info() # calling the global class function for the object
SBI.interest() # calling the global class function for the object