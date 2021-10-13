# Normal function which we use :
def add(a,b):
    return a-b
print(add(4,1))

# lamda or anonymous function which we are going to use for single line :
sub = lambda a,b: a-b
print(sub(4,2))
# sort function example
r=[1,2,5,13,88,45,54654,467468744,646464,46546,1146548686464,56464]
r.sort()
print(r)
# sort as lambda function :
rony=[[1,2],[7,8],[6,13],[15,29],[23,0]]
rony.sort(key= lambda fiza:fiza[1])
print(rony)