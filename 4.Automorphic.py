import math
n = int(input())
sqr = n * n
digits = int(math.log10(n)) + 1

rem = sqr % (10 ** digits)

if(rem == n):
    print("Automorphic")
else:
    print("Not Automorphic")
