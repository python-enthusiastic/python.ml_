import datetime
def gettime():
    return datetime.datetime.now()
def takevalue(r):
    if r==1:
        c = int(input("Enter value for 1 exercise or 2 for diet :\n"))
        if (c==1):
            value=input("type here :\n")
            with open("kapil_exe.txt",'a') as srk:
                srk.write(str([str(gettime())])+";"+value+"\n")
                print("exercise written sucessfully! thank you :")
        elif (c==2):
            value = input("type here :\n")
            with open("kapil_diet.txt",'a') as srk:
                srk.write(str([str(gettime())])+":"+value+"\n")
                print("your diet written sucessfully :")
    elif r==2:
        c = int(input("Enter value for 1 exercise or 2 for diet :\n"))
        if (c==1):
            value=input("type here :\n")
            with open("suraj_exe.txt",'a') as srk:
                srk.write(str([str(gettime())])+";"+value+"\n")
                print("exercise written sucessfully! thank you :")
        elif (c==2):
            value = input("type here :\n")
            with open("suraj_diet.txt",'a') as srk:
                srk.write(str([str(gettime())])+":"+value+"\n")
                print("your diet written sucessfully :")
    elif r==3:
        c = int(input("Enter value for 1 exercise or 2 for diet :\n"))
        if (c==1):
            value=input("type here :\n")
            with open("akash_exe.txt",'a') as srk:
                srk.write(str([str(gettime())])+";"+value+"\n")
                print("exercise written sucessfully! thank you :")
        elif (c==2):
            value = input("type here :\n")
            with open("akash_diet.txt",'a') as srk:
                srk.write(str([str(gettime())])+":"+value+"\n")
                print("your diet written sucessfully :")
        else:
            print("enter vallid number : 1 for kapil,2 for suraj ,3 for akash: \n")
def retrive(r):
    if r==1:
        c = int(input("enter 1 for exercise or 2 for diet :\n"))
        if (c==1):
            with open("kapik_exe.txt") as srk:
                for i in srk:
                    print(i,end="")
        elif (c==2):
            with open("kapik_diet.txt") as srk:
                for i in srk:
                    print(i, end="")
    elif r==2:
        c = int(input("enter 1 for exercise or 2 for diet :\n"))
        if (c==1):
            with open("suraj_exe.txt") as srk:
                for i in srk:
                    print(i,end="")
        elif (c==2):
            with open("suraj_diet.txt") as srk:
                for i in srk:
                    print(i, end="")
    elif r==3:
        c = int(input("enter 1 for exercise or 2 for diet :\n"))
        if (c==1):
            with open("akash_exe.txt") as srk:
                for i in srk:
                    print(i,end="")
        elif (c==2):
            with open("akash_diet.txt") as srk:
                for i in srk:
                    print(i, end="")
    else:
        print("enter valid detail press 1 for kapil , press 2 for suraj ,press 3 for akash")
print("health management created by ranjan singh :\n")
inp = int(input("press 1 for log or press 2 for retrive data :"))
if inp==1:
    b = int(input("press 1 for kapil , press 2 suraj , press 3 for akash :\n"))
    takevalue(b)
else:
    b = int(input("press 1 for kapil , press 2 suraj , press 3 for akash :\n"))
    retrive(b)