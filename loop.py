for i in range(10):
    print(i)
print("-----------------")
for i in range(1,6):
    print(i)
print("------------------")
for i in range(1,10,2):
    print(i)
print("----------------")
i=1
while i<=5:
    print(i)
    i+=1
print("--------------------")
for i in range(1,6):
    print(i)
print("----------even------------")
for i in range(1,21):
    if(i%2==0):
        print(i)
print("----------------------")
n = int(input("enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",i*n)
print("-------------------------")
n = int(input("Enter the number:"))
i=1
while i<=10:
    print(n,"X",i,"=",i*n)
    i+=1
print("-----------------------")
num = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{num} x {i}={i*num}")