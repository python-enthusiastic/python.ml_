def funcarg(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)

    print("this are some of our new member :")
    for key , value in kwargs.items():
        print(f"desgination of {key} is {value} ")
        # print(args)
normal = "hey! rony these are your fav periority list :\n"
lst=["rony","fiza","divyanshi","jinal","priya","kapil","payal","dhrasti :\n"]
hip = {"Ranjan":"Data scientist","Harry":"ui&ux","jinal":"banking","kapil":"artist"}
funcarg(normal, *lst , **hip)