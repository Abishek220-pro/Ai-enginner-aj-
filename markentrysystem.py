n = int(input("How many Student:"))
i =1
while i<=n:
    print("Student:",i)
    name = (input("name"))
    java = float(input("javamark"))
    python = float(input("python"))
    math=float(input("math"))
    total = float(java+python+math)
    average = (total/3)
    if average >=85:
       grade="A"
    elif average >=70:
        grade="B"
    elif average >=55:
        grade="C"
    else:
        grade="F"
    print("Enter the name:",name)
    print("Enter java mark:",java)
    print("Enter python mark:",python)
    print("Enter math mark:",math)
    print("Average:",f"{average:.2f}","-","Grade:",grade)
    i+=1






