print("Choose a question:")
print("1. Capital of Madhya Pradesh")
print("2. Capital of Rajasthan")
print("3. Capital of Tamil Nadu")
print("4. Capital of Uttar Pradesh")

choice = input("Enter question number (1-4): ")

if choice == "1":
    print("What is the captial of Madhya Pradesh?\n a) Chennai\n b) Jaipur\n c) Bhopal\n d) Lucknow")
    for i in range(3):
      answer = input("Enter your answer (a/b/c/d): ")
      if answer.lower() == "c":
         print("Correct! Bhopal is the capital of Madhya Pradesh.")
      else:
         print("Incorrect. The correct answer is Bhopal.")
elif choice == "2":
    print("What is the capital of Rajasthan?\n(a) Chennai\n(b) Jaipur\n(c) Bhopal\n(d) Lucknow")
    for g in range(3):
       answer = input("Enter your answer (a/b/c/d): ")
       if answer.lower() == "b":
          print("Correct!")
       else:
          print("Incorrect!")

elif choice == "3":
    print("What is the capital of Tamil Nadu?\n(a) Chennai\n(b) Jaipur\n(c) Bhopal\n(d) Lucknow")
    for e in range(3):
        answer = input("Enter your answer (a/b/c/d): ")
        if answer.lower() == "a":
          print("Correct!")
        else:
          print("Incorrect!")

elif choice == "4":
    print("What is the capital of Uttar Pradesh?\n(a) Chennai\n(b) Jaipur\n(c) Bhopal\n(d) Lucknow")
    for a in range(3):
        answer = input("Enter your answer (a/b/c/d): ")
        if answer.lower() == "d":
          print("Correct!")
        else:
          print("Incorrect!")

else:
    print("Invalid choice!")
