import math
n = int(input())
primes=[True]*(n + 1)
print(primes)
primes[0]= False
primes[1] = False

sqrt_n = int(math.sqrt(n))
for i in range(2,sqrt_n + 1):
    if primes[i]:
        for j in range(i * i, n + 1,i):
            primes[j] = False


for i in range(2,n + 1):
    if primes[i]:
        print(i)
