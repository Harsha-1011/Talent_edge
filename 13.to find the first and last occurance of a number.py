n = int(input())
arr = list(map(int,input().split()))
key = int(input())

def first_occuranceofnumber(arr,key):
    index1 = -1
    for i in range(n):
        if(key == arr[i]):
            index1 = i
            break
    return index1
def last_occuranceofnumber(arr,key):
    index2 = -1
    for i in range(n-1,-1,-1):
        if(key == arr[i]):
            index2 = i
            break
    return index2

print(first_occuranceofnumber(arr,key))
print(last_occuranceofnumber(arr,key))
