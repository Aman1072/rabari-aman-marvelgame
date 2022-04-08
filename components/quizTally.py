from components import vars

def total(value):

    if value == 20:
        vars.character = vars.characters[1]

        print("It's " + vars.character)

    if value == 30:
        vars.character = vars.characters[2]

        print("It's " + vars.character)

    if value == 50:
        vars.character = vars.characters[0]

        print("It's " + vars.character)

    if value == 100:
        vars.character = vars.characters[3]

        print("It's " + vars.character)                    