import time
runtime1 = time.time()

k=0
while(k<45):
    time.sleep(5)
    print("Hello data scientist :\n")
    k=k+1
print(f"time taken by while loop is {time.time()-runtime1} in second :\n")

initial = time.time()
for i in range(45):
    print("hey!RONY WILL YOU BE MINE :")
print(f"time taken by for loop is {time.time()-initial} in second :\n")

# #
# indiatime = time.asctime(time.localtime(time.time()))
# print(indiatime)