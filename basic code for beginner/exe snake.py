# import random
# i=0
# while(i<=10):
#     component=["snake","water","gun"]
#     rand = random.choice(component)
#     if rand == "snake":
#         enter = input("Enter anyone of them snake , water, gun :\n")
#         if enter == "water":
#             print("you loss : try again :")
#         elif enter == "gun":
#             print("congrats you win ")
#         elif enter== "snake":
#             print("match tied try again :")
#         else:
#             print("enter vaild option ")
#     if rand == "water":
#         enter = input("Enter anyone of them snake , water, gun :\n")
#         if enter=="snake":
#             print("congrates you win :")
#         elif enter=="gun":
#             print("sorry you loss :")
#         elif enter=="water":
#             print("match tied : try again:")
#         else:
#             print("enter valid option :\n")
#     if rand == "gun":
#         enter = input("Enter anyone of them snake , water, gun :\n")
#         if enter=="snake":
#             print("congrates you win :")
#         elif enter=="gun":
#             print("match tied try again :")
#         elif enter=="water":
#             print("sorry you loss :")
#         else:
#             print("enter valid option :\n")
#             break
# print("lets play snake water game :\n")
# i = print(10-i,"number are left comeone you can do it")
# i=i+1
# if (i>10):
#     print("game over")
#
#
#
import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
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

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#