# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

    # Converts the strings to lists.
    word = list(word)
    anagram = list(anagram)

    # Anagrams are not limited to one single word strings, this removes space keys or hyphens for easy manipulations.
    for i in word:
        if i == " " or i == "-":
            word.remove(i)

    for i in anagram:
        if i == " " or i == "-":
            anagram.remove(i)

    # Checks for the consistency in the number of letters in word and character.
    if len(word) != len(anagram):
        return False

    # Checks for the presence of every letter from the word in the anagram.
    for i in word:
        if not i in anagram:
            return False

    return True