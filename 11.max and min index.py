n = int(input())
arr = list(map(int,input().split()))

def find_maxindex(arr):
    max_ele = arr[0]
    index1 = 0
    for i in range(1,n):
        if(arr[i] > max_ele):
            max_ele = arr[i]
            index1 = i
    return index1
def find_minindex(arr):
    min_ele = arr[0]
    index2 = 0
    for i in range(1,n):
        if(arr[i] < min_ele):
            min_ele = arr[i]
            index2 = i
    return index2

print(find_maxindex(arr))
print(find_minindex(arr))
