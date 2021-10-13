n = 18
gusses=1
while (gusses<=9):
    inp = int(input("enter the number :"))
    if inp >18:
        print("number is greater  gusses again :\n ")
    elif inp < 18:
        print("number is smaller gusses again :\n")
    else:
        print("you won !you gusses right number:\n")
        break
    print(9-gusses,"number of gusses is left :\n")
    gusses = gusses+1
     #gusses=gusses+1
    if(gusses>9):
        print("game over")
