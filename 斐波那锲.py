def fibn(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        
        return fibn(n-1)+fibn(n-2)
a=50

s=fibn(a)
print(s)
