secret = 42
tries =0 
print("=== NUMBER GUESSIING GAME===")
while(True):
    guess = int(input("Guess the number:"))
    tries+=1
    if guess <secret:
        print("Too low!")
    elif guess>secret:
        print("Too high ! try again")
    else:
        print(f"Correct ! you got it in {tries}tries")
        break

    
