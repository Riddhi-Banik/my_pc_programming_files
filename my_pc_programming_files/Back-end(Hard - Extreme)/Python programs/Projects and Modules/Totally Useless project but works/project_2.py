import random as rd
try:
    _random_num, _guesses = rd.randint(1, int(input("Insert a number Range: "))), 0
    while True:
        _guess, _guesses = int(input("Make a guess: ")), _guesses + 1
        if _guess == _random_num:
            print(f"You guessed it! you made {_guesses} guesses")
            break
        print("Go big") if _guess < _random_num else print("Go small")
except:
    print("Something went wrong")