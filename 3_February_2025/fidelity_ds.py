l=[]
def sort(l):
    ''' This function is used to sort the List '''
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l