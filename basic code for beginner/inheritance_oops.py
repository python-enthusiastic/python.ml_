class college:
    no_of_student =43
    pass
# intance for  class
ty_computer_science = college()
sy_computer_science = college()

# intace for ty value add
ty_computer_science.name ="Rony"
ty_computer_science.roll_no = 24
ty_computer_science.subject = "Python"

# intace for sy class value add

sy_computer_science.name ="Fiza"
sy_computer_science.roll_no = 48
sy_computer_science.subject = "php"

print(ty_computer_science.no_of_student)
# what if we try to update no of student with intace class
ty_computer_science.no_of_student = 80
print(ty_computer_science.no_of_student)
print(ty_computer_science.__dict__)
print(college.no_of_student)
# as per this we can understand we can not  change or update value of class from intance class it only change then intance value
# only class can update by its self with the help class variable
# we cant update class variable from intace class object