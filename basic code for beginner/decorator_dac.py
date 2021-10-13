# # # def function1():
# # #     print("hello future data scientist :")
# # # func2 = function1
# # # del function1
# # # func2()
# #
# # # fucntion inside function:
# # def functrony(num):
# #     if num == 4:
# #         return print("asshole you are :")
# #     if num == 5:
# #         return sum
# # a= functrony(5)
# # print(a)
#
# # function as argument
#
# def executor(func):
#     func("rony is king ")
# executor(print)


# function decorator
def dec1(rony):
    def executi():
        print("program will be execute in shortly : ")
        rony()

        print("your program executed sucessfully : ")
    return executi
# with the help of @functname for executing this program:
@dec1
def mahadev():
    print(" mai tumhare saath hu :")
# mahadev = dec1(mahadev)
mahadev()

