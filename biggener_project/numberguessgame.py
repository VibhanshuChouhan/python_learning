num = int(input("Guess the number between 1 to 50: "))
while num != 17:
    if num < 17:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    num = int(input("Guess the number between 1 to 50: "))
          

print("Congratulations! You guessed the correct number.")