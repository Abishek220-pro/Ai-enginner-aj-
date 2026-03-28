name=input("Enter student name: ")
java = float(input("enter the java mark:"))
python = float(input("enter the python mark:"))
math = float(input("enter the math mark:"))
total = float(java+python+math)
average = total/3
if average >=85:
    grade="A"
elif average >=70:
    grade="B"
elif average >=55:
    grade="C"
else:
    grade="F"
print("-------Report Card----")
print("Student    :",name)
print("Java       :",java)
print("Python     :",python)
print("Math       :",math)
print("Total      :",total,"/",300)
print("Average    :",average)
print("Grade      :",grade)
print("----------------------")