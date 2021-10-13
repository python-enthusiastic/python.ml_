import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c = int(input("Enter 1 for exercise or Enter 2 for diet :\n"))
        if (c==1):
            value = input("type here \n")
            with open("ranjan_exe.txt",'a') as op:
                op.write(str([str(gettime())]) + " :" +value  +"\n")
                print("written sucssesfully")
        elif(c==2):
            value = input("type here :\n")
            with open("ranjan_diet.txt",'a') as op:
                op.write(str([str(gettime())]) + ":" + value +"\n")
                print("written diet sucssesfully")
    elif k==2:
        c=int(input("Enter 1 for exercise or Enter 2 for deit"))
        if (c==1):
            value = input("type here \n")
            with open("fiza_exe.txt",'a') as op:
                op.write(str([str(gettime())])+ ":"+ value +"\n")
                print("written exercise sucessfully ")
        elif (c==2):
            value =input("typer here :\n")
            with open("fiza_diet.txt",'a') as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("written diet sucessfully :")
    elif k==3:
        c = int(input("Enter 1 for exercise or Enter 2 for diet :\n"))
        if(c==1):
            value = input("ENTER HERE \n")
            with open("priya_exe.txt",'a') as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("written exersices sucessfully :")
        elif(c==2):
            value=input("enter here :\n")
            with open("priya_exe.txt",'a') as op:
                op.write(str([str(gettime())])+";"+value+"\n")
                print("written diet  sucessfully :")
        else:
            print("write valid input :")
def retrive(k):
    if k==1:
        c = int(input("enter 1 for exercise or 2 for diet :"))
        if (c==1):
            with open("ranjan_exe.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c==2):
            with open("ranjan_diet.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c = int(input("enter 1 for exercise or 2 for diet :"))
        if (c == 1):
            with open("fiza_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c==2):
            with open("fiza_diet.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c = int(input("enter 1 for exercise or 2 for diet :"))
        if (c == 1):
            with open("priya_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("priya_diet.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("enter valid number :")
print("health management system :\n")
num1= int(input("Enter 1 for log or enter 2 for retrive :\n"))
if num1==1:
    b = int(input("press 1 for ranjan 2 for fiza 3 for priya :\n"))
    take(b)
else:
    b = int(input("press 1 for ranjan press 2 for fiza  for priya press 3 :\n"))
    retrive(b)




