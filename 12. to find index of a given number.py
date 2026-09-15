n = int(input())
arr = list(map(int,input().split()))
key = int(input())
def findindexofnumber(arr,key):
    index = 1
    for i in range(len(arr)):
        if(key == arr[i]):
            index = i
    return index


print(findindexofnumber(arr,key))
    
    
