from random import choice
import math;

def repeatedSquaringModularExponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0 # n%1 == 0 always true
    remainder = 1 # we assume that the remainder is 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            remainder = (remainder * base) % modulus  # remainder is multiplied by base and we get the new remainder
        exponent = exponent // 2
        base = (base * base) % modulus  # continue squaring
    return remainder


def isPrime(n,k):
    if n%2==0:
        return False
    if n<3:
        return True
    
    t=n-1
    s=0
    while t%2==0:
        t=t/2
        s=s+1
    print("t=" + str(t) + "\ns=" + str(s))


    b=[]
    for i in range(0,k):
        a=choice([i for i in range(2,n) if i not in b])
        b.append(a)
        print("We have choose a="+str(a))
        b1=[]
        if repeatedSquaringModularExponentiation(a,t,n)==1:
            print(repeatedSquaringModularExponentiation(a,t,n))
            return True
        b1.append(repeatedSquaringModularExponentiation(a,t,n))
        print(b1)
        for d in range(1,s):
            b1.append(repeatedSquaringModularExponentiation(a,pow(2,d)*t,n))
            print(b1)
            if repeatedSquaringModularExponentiation(a,pow(2,d)*t,n)==1 and b1[-2]==n-1:
                return True
    return False


print(isPrime(409,3))