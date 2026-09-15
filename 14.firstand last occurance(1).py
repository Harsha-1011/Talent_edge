n = int(input())
arr = list(map(int,input().split()))
key = int(input())

def firstandlast(arr,key):
    f = -1
    l = -1
    for i in range(n):
        if(key == arr[i]):
            if(f == -1):
                f = i
            l = i
    return f,l
        
f, l = firstandlast(arr, key)

print(f)
print(l)
        
    
    
