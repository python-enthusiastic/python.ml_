# # marks = ["88","98","85","82","99"]
# # # use of mapping her with help of expression:
# # marks = list(map(int, marks))
# # marks[3] = marks[3] + 9
# # print(marks)
# #
# # # square function with the use of mapping
# #
# # squar = [2,3,4,5,6,7,8,9,10]
# #
# # # if you have to def sq fun you can create own function or use lambda also know as anonymous function:
# # #
# # # def sq(a):
# # #     return a*a
# # # squar = list(map(sq, squar))
# # # print(squar)
# #
# # # with the use of lambada function
# # squar = list(map(lambda x: x*x , squar))
# # print(squar)
# #
# #
# # # createing two function  for mapping
# # def square(a):
# #     return a*a
# # def cube(a):
# #     return a*a*a
# # func = [square,cube]
# # for i in range(100):
# #     val = list(map(lambda  x:x(i),func))
# #     print(val)
#
#
#
#
#
#
# # FILTER FUNCTION
# list1 = [12,12,1,1,25,6,789,7,7,35,46,479,7,654,87,9,476,7,987,65,98,796,87,687,8979]
# def greater(a):
#     return a>78
# greater = list(filter(greater,list1))
# print(greater)



# reduse function

from functools import reduce
marks =[34,49,44,38]


# with help of looop:
# tot = 0
# for i in marks:
#     tot = tot+i



# with help of reduse  function
tot = reduce(lambda x,y : x*y ,marks)
print(tot)