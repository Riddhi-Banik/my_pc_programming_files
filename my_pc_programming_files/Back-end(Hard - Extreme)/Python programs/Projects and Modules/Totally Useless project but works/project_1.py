print("Welcome to quiz game")  # Online quiz game 4 questions also have introduction
_inp, score = input("Do you want to play?: "), 0
if _inp.lower == "yes":
    quit()
print("Correct" if input("What is cpu?: ").lower() == "central processing unit" else "Incorrect")
print("Correct" if input("What is 3 + 1?: ") == "4" else "Incorrect")
print("Correct" if input("What is 4 - 1?: ") == "3" else "Incorrect")
print("Correct" if input("What is 1 * 7?: ") == "7" else "Incorrect")
