balance =10000
while(True):
    print("=======ATM MENU========")
    print("1.check balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")
    print("=======================")
    choice=int(input("Enter the choice:"))
    if choice==1:
        print(f"Your balance is:₹{balance}")
    elif choice==2:
        amount = int(input("Enter the deposite amount:"))
        balance+=amount
        print(f"₹{amount}deposited! New balance:₹{balance}")
    elif choice==3:
        withdraw=int(input("Enter the withdramount:"))
        if balance>withdraw:
            balance-=withdraw
            print(f"₹{withdraw}withdrawn! New balance:₹{balance}")
        elif balance<withdraw:
            print("Insufficient funds!")
    elif choice==4:
         print("Thank you good bye!")
         break



        


