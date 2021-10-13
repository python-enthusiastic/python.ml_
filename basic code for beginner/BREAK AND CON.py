"""i=0
print("Enter YOUR NUMBER :")
num=int(input())
while(True):
    if i+1>= num:
        i=i+1
        continue
    print(i+1)
    if (i==99):
        print("sucessfully enter numbeer less then 100:")
        break

    i=i+1"""
"""name =['rony','fiza','bhumi','akash','vipin','roshni']
print(type(name))
print("enter your name :")
r1=input()
for items in range(len(name)):
        print(name[items])
        if name[items]==r1:
            print("name found in list")
            break
            print("loop terminaated")"""

while(True):
    num1=int(input("Enter your number :"))
    if num1>100:
        print("congrats you have enter number greater then100 \n")
        break
    else:
        print("try agaim \n")
        continue