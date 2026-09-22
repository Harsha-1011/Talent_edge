s = 'Salapuvanipalem'
freq = {}
for ch in s:
    freq[ch]=freq.get(ch,0)+1


sorted_list = sorted(s,reverse = True)
print(sorted_list)

result = sorted(freq.items(),key = lambda x:x[1],reverse = True)
print(result)
