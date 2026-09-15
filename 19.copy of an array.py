arr = list(map(int, input().split()))
dup_arr = []

for i in range(len(arr)):
    dup_arr.append(arr[i])

for ele in arr:
    print(ele, end=" ")

print()

for ele in dup_arr:
    print(ele, end=" ")
