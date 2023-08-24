input = "geeksforgeeks portal"
name = "james mumo"


# fun to chek vowel and keep count
# then increment with case
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def countVowels(word):
    count = 0
    for i in word:
        if isVowel(i):
            count += 1
    return count


print(countVowels(input))
print(countVowels(name))
