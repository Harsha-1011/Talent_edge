s = input()
i = 1
words = s.split(" ")
for word in words:
    print(i,word,len(word),vowel(word),consonet(word))
    i += 1

