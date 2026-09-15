s = input()
upper_count = 0
lower_count = 0
for ele in s:
    if ele.isupper():
        upper_count += 1
    else:
        lower_count += 1
print(upper_count,lower_count)
