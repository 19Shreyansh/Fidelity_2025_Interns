data=100
'''Example of Functions to be imported in different moduldes.'''
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def rev(n):
    ans = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        ans = ans * 10 + digit
    return ans