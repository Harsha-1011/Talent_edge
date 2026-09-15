s = input()
lower = 0
upper = 0
symbol = 0
for ch in s:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    else:
        symbol += 1
print(lower)
print(upper)
print(symbol)
