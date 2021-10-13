# code for write text in file
# f =open("ranjan.txt",'w')
# constent= f.write("damn cool\n")
# print(constent)
# f.close()


# for append file code
# f =open("ranjan.txt",'a')
# constent= f.write("damn cool\n")
# print(constent)
# f.close()

f= open("ranjan.txt",'r+')
contant=f.read()
contant=f.write("thank you guy's")
print(contant)
f.close()