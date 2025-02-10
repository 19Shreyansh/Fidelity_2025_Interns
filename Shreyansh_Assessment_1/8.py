'''Name = Shreyansh Srivastava'''
'''Questions = 1,4,7,8,10'''
'''Email Address = shreyanshsri19@gmail.com'''

import time
import random

def time_decorator(fun): #dedcorator method
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res=fun(*args,**kwargs)
        end_time = time.time()
        print(f"{fun.__name__} took time {end_time-start_time : 6f} seconds")
        return res
    return wrapper

@time_decorator
def Bubble_Sort(l): # bubble sort method 
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l    

@time_decorator
def Sequential_Search(l,x): # Sequential Search method 
    for i,v in enumerate(l):
        if v==x:
            print("Found at index : ",i)
            return
    print("f{x} is not found")

m=[random.randint(1,10000) for _ in range (500)] # takes random numbers as input 
t=m.copy()     # make a copy of the list
Bubble_Sort(m)  # sort the list
print("Sorted Array is : ",m)   # display the sorted list

Sequential_Search(t,7777)   # search an element in the unsorted list beacuse we made a copy