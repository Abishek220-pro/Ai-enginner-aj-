n = int(input("How many subjects: "))
mark=[]
for i in range(n):
    marks=int(input(f"Enter the mark{i+1}:"))
    mark.append(marks)
print(mark)
print("Highest:",max(mark))
print("Lowest:",min(mark))
print("Total",sum(mark))
avg = sum(mark)/len(mark)
print(f"Average:{avg:.2f}")