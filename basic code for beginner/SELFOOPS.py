class computer_science:
    # def printdetail(self):
    #     return f"MY NAME IS {self.name} , MY ROLL NO IS {self.roll_no} , I AM WORKING WITH {self.organization} "
    def __init__(self,name,roll_no,organization ):
        self.name = name
        self.roll_no = roll_no
        self.organization = organization
# developer = computer_science()
data_scientist = computer_science("Fiza shaikh",48,"Advocate")
# this argument always passes in init function  whatever we write here it will go in __init__(constructor) if we dont create
# __init__ function then we can not pass argument in intance class:
print(data_scientist.__dict__)
# now i'll put name roll number and organization

developer.name = "ABHISHEK CHAUDHARY "
developer.roll_no = 3
developer.organization = "Microsoft India"

data_scientist.name ="RANJAN SINGH "
data_scientist.roll_no = 24
data_scientist.organization = "IBM"
print(developer.printdetail())

#
#
#
#
#
#
# # example done by me
#
#
# class anonymous:
#     def __init__(self,first_number,second_number):
#         self.first_number = first_number
#         self.second_number = second_number
#     def inputdetail(self):
#         print("First number = " + str(self.first_number))
#         print("Second number = " + str(self.second_number))
#         print("Addition of two numbers = " + str(self.answer))
#
#     def sum_of_num(self):
#         self.answer= self.first_number+self.second_number
# addi = anonymous(45124646468,1346874346873214)
# print(addi.sum_of_num(
# ))
# # print(addi.inputdetail())

def xyz():
    return tot+1
tot =0
print(xyz())