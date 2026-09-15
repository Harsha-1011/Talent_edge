def swapAdjacent(arr):
    for i in range(0,len(arr)-1,2):
        arr[i],arr[i + 1] = arr[i + 1],arr[i]

arr = list(map(int,input().split()))
for ele in arr:
    print(ele,end = " ")
print()
swapAdjacent(arr)
for ele in arr:
    print(ele,end = " ")
    
