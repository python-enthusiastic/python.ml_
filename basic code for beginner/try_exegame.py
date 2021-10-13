import random
component=["s","w","g"]

human_point =0
computer_point = 0
chance = 10
no_of_chance = 0
print("\t  \t \t snake water gun :")
print("s for snake, w for water , g for gun ")

while no_of_chance < chance:
    enter = input("snake,water,gun :")
    rand = random.choice(component)
#     # for s input
#     if enter == "s" and rand == "w":
#         human_point = human_point+1
#         print(f" gusses of human {enter},gusses of computer {rand}:\n")
#         print("human win")
#         print(f" your point is {human_point} computer point is {computer_point}")
#     elif enter == "s" and rand == "g":
#         computer_point = computer_point + 1
#         print(f" gusses of human {enter},gusses of computer {rand}:\n")
#         print("computer win")
#         print(f" your point is {human_point} computer point is {computer_point}")
#     # for w input
#     elif enter == "w" and rand == "g":
#         human_point = human_point+1
#         print(f" gusses of human {enter} gusses of computer {rand}")
#         print("human wins :")
#         print(f" your point is {human_point} computer point {computer_point} ")
#     elif enter == "w" and rand == "s":
#         computer_point = computer_point + 1
#         print(f" gusses of human{enter} gusses of computer {rand}")
#         print("human wins :")
#         print(f" your point is {human_point} computer point {computer_point} ")
#     # for g input
#     elif enter == "g" and rand == "w":
#         computer_point = computer_point + 1
#         print(f" gusses of human{enter} gusses of computer {rand}")
#         print("computer wins :")
#         print(f" your point is {human_point} computer point {computer_point} ")
#     elif enter == "g" and rand == "s":
#         human_point = human_point + 1
#         print(f" gusses of human {enter} gusses of computer {rand}")
#         print("computer wins :")
#         print(f" your point is {human_point} computer point {computer_point} ")
#     else:
#         print("enter vaild option :\n")
# no_of_chance = no_of_chance+1
# print(f"{chance - no_of_chance} is left out of {chance}")
# print("game over:")
# if computer_point == human_point:
#     print("tied")
# elif computer_point > human_point:
#     print("computer win : try again")
# else:
#     print("congrates ypu win this game")
# print(f"your point{human_point} computer point {computer_point}")
    if enter == rand:
        print("Tie Both 0 point to each \n ")

    elif enter == "s" and rand == "g":
        computer_point = computer_point + 1
        print(f"your guess {enter} and computer guess is {rand} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif enter == "s" and rand == "w":
        human_point = human_point + 1
        print(f"your guess {enter} and computer guess is {rand} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif enter == "w" and rand == "s":
        computer_point = computer_point + 1
        print(f"your guess {enter} and computer guess is {rand} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif enter == "w" and rand == "g":
        human_point = human_point + 1
        print(f"your guess {enter} and computer guess is {rand} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif enter == "g" and rand == "s":
        human_point = human_point + 1
        print(f"your guess {enter} and computer guess is {rand} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif enter == "g" and rand == "w":
        computer_point = computer_point + 1
        print(f"your guess {enter} and computer guess is {rand} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")