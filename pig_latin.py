# Task: Write a program in a file called `pig_latin.py` that take a string called `text` which is a single valid English word without spaces or special characters and translates the text to Pig Latin. In Pig Latin:

# If a word starts with a single consonant before the first vowel, move the first letter to the end and add "ay" to the end of the word.
# If a word starts with a consonant cluster i.e. more than one consonant before the first vowel, move the consonant cluster to the end and add “ay” to the end of the word.
# If the consonant cluster that starts the word ends with ‘y’, `y` is considered a vowel and therefore remains at the beginning with the rest of string, followed by the consonant or consonant cluster and then “ay” at the end of the word.
# If `y` however starts the word, it is considered a consonant and follows the first rule.
# If a word starts with a vowel, add "way" to the end of the word.

import string


vowels = ["a", "e", "i", "o", "u", "y"]
consonant_letters = list(set(string.ascii_lowercase) - set(vowels))
text = input("Enter a text: ").strip().lower()

if text[0] == "y":
    result = text[1:] + "y" + "ay"

if text[0] in vowels:
    result = text + "way"


else:
    i = 0

    while i < len(text):
        char = text[i]
        if char in vowels :
            result = text[i:] + text[:i] + "ay"

        i += 1

    result = text + "ay"

print(f" The results is {result}")


# Task: Write a program in a file called `pig_latin.py` that take a string called `text` which is a single valid English word without spaces or special characters and translates the text to Pig Latin. In Pig Latin:

# If a word starts with a single consonant before the first vowel, move the first letter to the end and add "ay" to the end of the word.
# If a word starts with a consonant cluster i.e. more than one consonant before the first vowel, move the consonant cluster to the end and add “ay” to the end of the word.
# If the consonant cluster that starts the word ends with ‘y’, `y` is considered a vowel and therefore remains at the beginning with the rest of string, followed by the consonant or consonant cluster and then “ay” at the end of the word.
# If `y` however starts the word, it is considered a consonant and follows the first rule.
# If a word starts with a vowel, add "way" to the end of the word.

import string

def pig_latin(text):

    vowels = ["a", "e", "i", "o", "u", "y"]
    consonant_letters = list(set(string.ascii_lowercase) - set(vowels))

    if text[0] == "y":
        return text[1:] + "y" + "ay"

    if text[0] in vowels:
        return text + "way"

    else:
        i = 0

        while i < len(text):
            char = text[i]
            if char in vowels :
                return text[i:] + text[:i] + "ay"

            i += 1

        return text + "ay"

print(pig_latin(input("Enter a text: ").strip().lower()))


