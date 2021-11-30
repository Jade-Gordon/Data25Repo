# String basics

# print(type("hello world"))
# print(type('hello again'))

print(u'\u0061') # this returns "a". This is actually the unit code of "a"
# This is important to know because Python doesn't see words, sentences or paragraphs.

print("hello world"[1])    # this prints the letter e as this is in index 1
print("hello world"[-1])    # this prints the letter d, the last character in the string.
# [-2] gives the penultimate character
print(len("hello world"))   # this prints the length of the string, the total amount of letters
