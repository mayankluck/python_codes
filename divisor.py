from math import sqrt
def div(n):
    div=set()
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            div.add(i)
            div.add(n//i)
    return div

t= int(input())
while t:
    n= int(input())
    print("divisor of {} is ({})".format(n,div(n)))
    t=t-1