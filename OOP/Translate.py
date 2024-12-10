def translate(phrase):
    translation = ""
    for i in phrase:
        if i  in "aeiouAEIOU":
            if i.isupper():
                translation += "g"
            else:
                translation += "g"
        else:
            translation += i
    return translation


print(translate(input("Enter a phrase: ")))
