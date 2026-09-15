n = int(input())
k = n
sum = 0
prod = 1
while(n > 0):
    rem = n % 10
    sum = sum + rem
    n = n//10
print(sum)


n = k
while(n > 0):
    rem = n % 10
    prod = prod * rem
    n = n//10
print(prod)
if(sum == prod):
    print("spy number")
else:
    print("Not spy number")
