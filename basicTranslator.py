def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                letter = "G"
            else:
                letter = "g"
        translation = translation + letter
    return translation


# This program will change all vowels passed to the translator to a g
print(translate(input("Enter a phrase to translate: ")))
