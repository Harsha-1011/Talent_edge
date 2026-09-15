n = int(input())
cube_n = n**(1/3)
print(cube_n)
if(cube_n * cube_n * cube_n == n):
    print("perfect cube")
else:
    print("Not a perfect cube")
    
