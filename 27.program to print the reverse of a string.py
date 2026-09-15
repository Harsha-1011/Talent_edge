def findReverse(word):
   output = ""
   for ch in word:
       output = ch + output
   return output

s = input()
words = s.split()

for word in words:
    reverse = findReverse(word)
    print(word,reverse)
