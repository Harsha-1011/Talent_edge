def findNonRepeatingCharacter(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1;
    for ch in s:
        if(freq.get(ch) == 1):
            return ch;

s = input()
print(findNonRepeatingCharacter(s))
