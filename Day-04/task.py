student ={
        "name":"Abishek",
        "roll":"24CY002",
        "subjects":{"python","DSA","MERN","AI"}
}
print(student["name"])
print(student["roll"])
student["subjects"].remove("MERN")
student["subjects"].add("Cloud")
for subject in student["subjects"]:
    print(subject)
print("DSA" in student["subjects"])