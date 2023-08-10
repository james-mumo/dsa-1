# reverse the word "Too Many Nighst"

word = "Jungle Man"

def reverseMe(word):
    splitWord = word.split()
    stack = []

    for w in splitWord:
        stack += w

    reversedWord = ""

    while stack:
        reversedWord += stack.pop()

    return reversedWord

print(reverseMe("James Mumo"))