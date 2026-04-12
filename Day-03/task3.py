n=int(input("How many Students: "))
studentlist =[]
for i in range(n):
    name = input(f"Student {i+1} name: ")
    total =0
    for j in range(n):
        marks=int(input(f"Enter marks{j+1}: "))
        total+=marks
    avg = total/n
    if avg>=80:
        grade ="A"
    elif avg>=60:
        grade="B"
    else:
        grade="C"
    studentlist.append([name,avg,grade])
print("=======CLASS REPORT========")
for i in range(n):
    print(f"{i+1}.{studentlist[i][0]}|Avg:{studentlist[i][1]:.2f}|Grade:{studentlist[i][2]}")


