balance = 1000.00 

while True:
     print("Welcome to the ATM!")
     print("1. Check Balance")
     print("2.Deposit")
     print("3. Withdraw")
     print("4. Exit")
     
     choice = input("Please select an option: ")
     
     if choice == '1':
         print(f"Your current balance is: ${balance:.2f}")
     elif choice == '2':
         deposit_amount = float(input("Enter amount to deposit: "))
         balance += deposit_amount
         print(f"${deposit_amount:.2f} deposited. New balance: ${balance:.2f}")
     elif choice == '3':
         withdraw_amount = float(input("Enter amount to withdraw: "))
         if withdraw_amount <= balance:
             balance -= withdraw_amount
             print(f"${withdraw_amount:.2f} withdrawn. New balance: ${balance:.2f}")
         else:
             print("Insufficient funds.")
     elif choice == '4':
         print("Thank you for using the ATM. Goodbye!")
         break
     else:
         print("Invalid option selected. Please try again.")