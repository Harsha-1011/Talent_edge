def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b
x,y = map(int,input().split())
sum = add(x,y)
diff = sub(x,y)
pro = mul(x,y)
division = div(x,y)

print(sum,diff,pro,division)
