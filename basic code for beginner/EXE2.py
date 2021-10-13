print("Insert First number :")
num1=int(input())
print("Insert second number :")
num2=int(input())
print("select the task which you have to perform +,*,-,?,% :")
num3=input()
if num1==45 and num2==3 and num3=='*':
    print(555)
elif num1==56 and num2==9 and num3=='+':
    print(77)
elif num1==56 and num2==6 and num3=='/':
    print(4)
elif num3=='*':
    print("multiplication of this two number is : ",num1*num2)
elif num3=='+':
    print("add of this two number is : ",num1+num2)
elif num3=='-':
    print("sub of this two number is : ",num1-num2)
elif num3=='%':
    print("mod of this two number is : ",num1%num2)
elif num3 == '/':
    print("div of this two number is : ", num1 / num2)

