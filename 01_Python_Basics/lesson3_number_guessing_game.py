secret_number = 7

while True:
    guess  = int(input("Guess the secret number (1-10): "))
    
    if guess == secret_number:
        print("Correct!")
        break

    elif guess < secret_number:
        print("Too low!")

    else: 
        print("Too high!")

        