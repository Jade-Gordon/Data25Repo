def anagrams(word1, word2):
    #word = sorted("ebony")
    if sorted(word1) == sorted(word2):
        return True
    return False

#ebony -> boney
print(anagrams("ebony", "boney"))
