import random
print("Welcome to the Number Gussing Game!")

low = 1
high = 10

print("Think of a number between 1 to 10 and computer will be guess it.🤔")

if low <=high:
    guess = random.randint(low, high)
    print("Computer's guess is: ", guess)

    while True:
        feedback = input("Is the guess too high (H), too low (L),or correct (C)? ").strip().upper()

        if feedback == "C":
            print("Yay! 🎉 Computer  guessed your number✔ ")
            break
        elif feedback == "H":
            high = guess - 1
            guess = random.randint(low, high)
            print("Computer's guess is: ",guess)
        elif feedback == "L":
            low = guess + 1
            guess = random.randint(low, high)
            print("Computer's guess is: ",guess)
        else:
            print("Please enter H, L, or C.")
if low > high:
    print("Invalid range. Please try again.")







