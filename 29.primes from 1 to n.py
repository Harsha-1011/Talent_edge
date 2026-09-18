import math
def isprime(n):
    sqt_n = int(math.sqrt(n))
    for i in range(2,sqt_n + 1):
        if(n%i == 0):
            return False
        
    return True
n = int(input())
for i in range(2,n + 1):
    if(isprime(i)):
        print(i)
