
def ispowerof2(n):
    if n <=0:
        return False
    x=n
    y= not(n &(n-1))
    return x and y


t= int(input())
while t:
    n= int(input())
    print(ispowerof2(n))
    t= t-1    