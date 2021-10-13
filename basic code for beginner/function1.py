#user define function
def addfun():
    """This function is created for finding average no of two variable :"""
    a=int(input("enter value for a :\n"))
    b=int(input("enter value for b :\n"))
    average=(a+b)/2
    return average
print(addfun.__doc__)
r= addfun()
print(r)
