class student:
    no_of_subject = 8
    def __init__(self,name,roll_no,subject):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject
# if i have to update class from inside intance then i can use classmethod for it
    @classmethod
    def change_subject(cls,new_subject):
        cls.no_of_subject = new_subject


# computer_science = student
cs= student("ranjan singh",45,"python")
print(cs.__dict__)
cs.change_subject(45)
print(student.no_of_subject)
# if i have to update class from inside intance then i can use classmethod for it



cs.no_of_subject = 45
student.no_of_subject
print(student.no_of_subject)
