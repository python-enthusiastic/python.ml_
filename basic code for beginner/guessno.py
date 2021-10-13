r=18
number_gusses=1
while(number_gusses<9):
    num1=int(input("Please gusses the number :"))
    if num1>18:
        print("number is greater plz gusse smaller number :")
    elif num1<18:
        print("number is too smaller plz gusse again :")
    else:
        print("congratulation you gusse correct number")
        break
    if(number_gusses<9):
        print(9 - number_gusses, "number of attempt left :")
        number_gusses = number_gusses+1
