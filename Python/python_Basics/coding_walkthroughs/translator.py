"""
J Language
vowels -> j
------------
dog -> djg
cat -> cjt
"""
def translate(phrase):
    translation = ""
    for letter in phrase:
        # want to check if a letter is(not) a vowel
        # more efficient way of coding for lowercase letters
        # initially had "AEIOUaeiou"
        if letter.lower() in "aeiou":
        # If a vowel in the phrase is UPPER CASE, return "J"
            if letter.isupper():
                translation = translation + "J"
            translation = translation + "j"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))