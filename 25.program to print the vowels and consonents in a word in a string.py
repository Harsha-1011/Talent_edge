def vowel(word):
    count = 0
    for ch in word:
        if(ch in "aeiouAEIOU"):
            count += 1
    return count

def consonent(word):
    count = 0
    for ch in word:
        if(ch.isalpha() and ch not in "aeiouAEIOU"):
            count += 1
    return count
    
s = input()
i = 1
words = s.split(" ")
for word in words:
    print(i,word,len(word),vowel(word),consonent(word))
    i += 1
