n = int(input())
arr = list(map(int,input().split()))
key = int(input())
count = 0
for ele in arr:
    if key == ele:
        count+=1
print(count)
    
