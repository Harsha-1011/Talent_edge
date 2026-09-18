import math
n = int(input())
sqrt_n = int(math.sqrt(n))
factors = {}
for i in range(2,sqrt_n + 1):
    while(n % i == 0):
        factors[i] = factors.get(i,0)+1
        n = n/i
    if n == 1:
        break

if(n > 1):
    factors[i] = factors.get(n,0)+1
    print(factors)
