def isPalindrome(str):
    newStr = ""

    for c in str:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


str = "ana"
print(isPalindrome(str))
