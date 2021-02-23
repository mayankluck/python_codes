def sum_n(n):
    return (n*(n+1))//2


t= int(input("enter the test case"))
while t:
    n=int(input())
    print("sum of {} natural numbers is {}".format(n, sum_n(n)))
    t= t-1