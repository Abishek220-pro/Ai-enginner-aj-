student ={"name":"Abishek","Age":19,"college":"MEC"}
print("----------")
print(student["name"])
print("-----------")
student["city"]="tiruppur"
student["Age"]=20
del student["college"]
print(student)
print("---------------------")
print(student.keys())
print(student.values())
print(student.items())
print("------------------------------")
for key,value in student.items():
    print(key,"=>",value)
