# using basic method for count 1 in binary
def binary(a):
    binary=[]
    while a:
        binary.append(a%2)
        a=int(a//2)
    x=str(binary)
    return x.count("1")
# ------------------------------------------
# using bruteforce method with bin library
def bruteforcecnt(n):
    s =(bin(n))         #bin() is a pre define library to convert into binary
    print("{}".format(s))

    return s.count('1')
#-------------------------------------------------------
#using complex or tricky method 
def cntbits(n):
    cnt =0
    while n:
        cnt+=1
        n = n & (n-1)
    return cnt


t= int(input())
while t:
    n=int(input())
    print("no of 1 in {} in binary ={}".format(n,binary(n)))
    print("no of 1 in {} in binary ={}".format(n,bruteforcecnt(n)))
    print("no of 1 in {} in binary ={}".format(n,cntbits(n)))
    t=t-1