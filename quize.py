from components.quizQuestions import questions
from components import vars, quizTally

player_choice = False
player_choice = True

while player_choice is True:

    print("~~~~~~~~~~~~~~~~~~~~ WELCOME TO MARVEL GAME.~~~~~~~~~~~~~~~~~~~\n")

    answer1 = questions["q1"][input(questions["q1"]["question"])]
    print(answer1)

    vars.quizTotal += answer1
    print("*****************************************************************\n")

    answer2 = questions["q2"][input(questions["q2"]["question"])]
    print(answer2)

    vars.quizTotal += answer2
    print("******************************************************************\n")

    answer3 = questions["q3"][input(questions["q3"]["question"])]
    print(answer3)

    vars.quizTotal += answer3
    print("*******************************************************************\n")

    answer4 = questions["q4"][input(questions["q4"]["question"])]
    print(answer4)

    vars.quizTotal += answer4
    print("*******************************************************************\n")

    answer5 = questions["q5"][input(questions["q5"]["question"])]
    print(answer5)

    vars.quizTotal += answer5
    print("*******************************************************************\n")

    print("total so far: " + str(vars.quizTotal) + "\n")
    quizTally.total(vars.quizTotal)

    print("Hey, would like try one more time and try get different character?")
    choice = input("Yes/No? ")

    if choice == "Y" or choice == "y":
        choice == True

    if choice == "N" or choice == "n":
        print("you choose quite!! Because you did not got your fav. character.")
        exit()    
