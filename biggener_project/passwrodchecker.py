password = "0000"

for a in range(5):
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break 
    else:
        print("Access denied! Try again.")

else:
    print("Too many failed attempts. Access denied.")