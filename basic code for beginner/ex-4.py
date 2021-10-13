# if we dont pass integer at input time it will not take 0 or 1 as integer but  it take as string and draw star partten from up-side down
print("Enter how many row you want to print :\n")
row = int(input())
print("argument you want to print 1 or 0 :\n")
argument = int(input())
constent = bool(argument)
if constent == True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
elif constent == False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()