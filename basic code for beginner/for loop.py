"""list1=[1,2,3,4,5,6]
dict1={"rony":"singh","akash":"singh","bhumi":"singh","roshni":"singh"}
print("ENTER YOUR NAME :")
NAME1=input()
for name ,surname in dict1.items():
    if NAME1 =='rony':
        print(name,surname)
    else:
        print("no data found")"""
list1=["ranjan",1,2,33,44,4,7,58,"singh","fiza"]
for number in list1:
    if str(number).isnumeric() and number>6:
        print(number)
    else:
        print("no number found")