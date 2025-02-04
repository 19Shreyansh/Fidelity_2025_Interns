def f1(fun):
    def wrapper():
        print("Hello")
        fun()
        print("End")
    return wrapper
@f1
def  f2():
    print("Fidelity Items")
f2()

def f1(fun):
    def wrapper(a,b):
        print("Adding")
        fun(a,b)
        print("End")
    return wrapper
@f1
def add(x,y):
    print("Sum is : ",x+y)
add(10,20)