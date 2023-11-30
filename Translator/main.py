def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.upper() in "AUOIE":
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
