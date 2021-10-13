import random
lst = ["s","w","g"]


chance = 10
human_point=0
computer_point=0
no_of_chance =0

print("PRESS S FOR SNAKE\nPRESS W FOR WATER\nPRESS G FOR GUN \n ")
print("\t\t\t",lst)
while no_of_chance < chance:
    gusses = input("press s for snake, press w for water ,press g for gun :\n")
    random_comp = random.choice(lst)


    if gusses == random_comp:
        print(f"you both gusses same so match tied user point {human_point} computer point are {computer_point} :")

        # user input
    elif gusses == "s" and random_comp == "w":
        human_point = human_point+1
        print(f"Congratulation you win this game your  gusse is {gusses} and computer gusses is {random_comp} :\n")
        print(f"user point are  {human_point} computer point are {computer_point}")
    elif gusses == "s" and random_comp == "g":
        computer_point = computer_point+1
        print(f"soryy you loss your gusse was {gusses} and computer gusses was{random_comp}")
        print(f"user point are  {human_point} computer point are {computer_point}")

        #for water input
    elif gusses == "w" and random_comp == "g":
        human_point=human_point+1
        print(f"Congratulation you win this game your  gusse is {gusses} and computer gusses is {random_comp} :\n")
        print(f"user point are  {human_point} computer point are {computer_point}")
    elif gusses == "w" and random_comp == "s":
        computer_point=computer_point + 1
        print(f"soryy you loss your gusse was {gusses} and computer gusses was{random_comp}")
        print(f"user point are  {human_point} computer point are {computer_point}")


        # user input for g

    elif gusses == "g" and random_comp == "s":
        human_point = human_point + 1
        print(f"Congratulation you win this game your  gusse is {gusses} and computer gusses is {random_comp} :\n")
        print(f"user point are  {human_point} computer point are {computer_point}")
    elif gusses =="g" and random_comp == "w":
        computer_point = computer_point + 1
        print(f"soryy you loss your gusse was {gusses} and computer gusses was{random_comp}")
        print(f"user point are  {human_point} computer point are {computer_point}")
    else:
        print("Enter valid detail : select correct option \n")
    no_of_chance = no_of_chance+1
    print(f"{chance- no_of_chance} are left out of {chance}")
print("game over \n")
if human_point == computer_point:
    print(("Match tied you both score same :"))
elif human_point>computer_point:
    print(f"congratulation you win this game and your points are{human_point}")
else:
    print(f"sorry you losss this game :\n")
print(f"your point are {human_point} and computer points are {computer_point}")

