def bin(a):
    binary=[]
    while a:
        binary.append(a%2)
        a=int(a//2)
    return binary

t= int(input())
while t:
    n=int(input())
    x=bin(n)
    x.reverse()
    print(x)
    t=t-1