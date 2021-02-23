from math import sqrt
def prime1(n):
    div=set()
    if n==0 or n==1:
        return False
    for i in range(1, int(sqrt(n)+1)):
        if n%i==0:
            div.add(i)
            div.add(n%i)  #no need to take this because this is a also a factor of n%i
    if len(div)>2:
            return False
    else:
        return True


def prime2(n):
    div=set()
    if n==0 or n==1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            return False
            break
    return True



t=int(input())
while t:
    n= int(input())
    print(prime1(n))
    print(prime2(n))
    t=t-1