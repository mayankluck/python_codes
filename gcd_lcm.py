def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(n,m):
    prod=n*m
    return prod // gcd(n,m)


t=int(input("enter test case"))
while t:
    n, m = map(int,input().split())
    print("gcd={} Lcm={}".format(gcd(n,m),lcm(n,m)))
    t = t-1