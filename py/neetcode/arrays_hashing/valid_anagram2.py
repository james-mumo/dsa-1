# sol 1 with hash_set

def validAnagram(s, t):
    return Counter(s) == Counter(t)

t = "james"
s = "semaj"

print(validAnagram(s, t))
