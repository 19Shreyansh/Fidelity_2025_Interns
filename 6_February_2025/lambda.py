#functional progamming = one line functions eg arrow function
#parameters can be n numbers but expr can be only 1
#lambda parameters : expr 
#        (n1,n2)

#def add(x,y):
#    return x+y

#add is not a variable 
add=lambda x,y:x+y
print(add(10,20))


# map() = higher order function . its parameter is a function and iterable
#higher order function takes function as its parameters

#map(f1,iterable) . map returns a value

price=[10,20,30,40,50,60]
add=100
def add_value(x):
    return x+add
new_value=map(add_value,price)
print(list(new_value))
nv=map(lambda x:x+add,new_value)
print(list(nv))

#filter returns a boolean value

#ag=lambda x:'even' if x%2==0 else 'odd'
#print(ag)
age=[11,23,18,30,40]
def age_list(x):
    return x>18
    #     return True
    # else:
    #     return False

a=filter(age_list,age)
print(list(a))

age_list=list(filter(lambda x:x>18,age))
print(list(age_list))