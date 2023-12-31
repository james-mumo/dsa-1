# sol 1 with hash_set

def validAnagram(s, t):
   return sorted(s) == sorted(t)


t = "james"
s = "semaj"

print(validAnagram(s, t))
