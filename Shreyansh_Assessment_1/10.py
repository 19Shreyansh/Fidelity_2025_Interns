'''Name = Shreyansh Srivastava'''
'''Questions = 1,4,7,8,10'''
'''Email Address = shreyanshsri19@gmail.com'''

class convert:
    def __init__(self,dictionary):  # dictionary argument is passed
        self.dictionary=dictionary

    def keys(self): # keys function
        return list(self.dictionary.keys())
    
    def values(self):   # values function 
        return list(self.dictionary.values())
    
    def dsp(self):  # display method for keys and values
        print("Keys are : ",self.keys())
        print("Values are : ",self.values())

data = {"Name":"Shreyansh","Age":23,"City":"Lucknow","Sports":"Football","Favourite Dish":"Chicken"}
obj=convert(data)   # object creation for dictionary
obj.dsp()   # display method for the object