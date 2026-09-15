n = int(input())
arr = list(map(int,input().split()))

def findmax(arr):
    max_ele = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] > max_ele):
            max_ele = arr[i]
    return max_ele
def findmin(arr):
    min_ele = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] < min_ele):
            min_ele = arr[i];
    return min_ele
print(findmax(arr))
print(findmin(arr))
