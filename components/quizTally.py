from components import vars

def total(value):

    if value <= 10:
        vars.character = vars.characters[0]

        print("It's " + vars.character)

    if value >= 20:
        vars.character = vars.characters[1]

        print("It's " + vars.character)

    if value <= 0:
        vars.character = vars.characters[2]

        print("It's " + vars.character)        