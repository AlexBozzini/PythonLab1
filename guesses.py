def get_secret_number():
    import random
    secret_number = random.randint(1, 101)
    return secret_number


def guessing_game():
    attempts_count = 0
    success = False
    secret_number = get_secret_number()
    while not success:
        guess = int(input("Guess a number between 1 and 100."))
        if guess > secret_number:
            print("Too high!")
            attempts_count = attempts_count + 1
        elif guess < secret_number:
            print("Too low!")
            attempts_count = attempts_count + 1
        else:
            if attempts_count == 1:
                print("You win! It took you 1 try.")
            else:
                print("You win! It took you", attempts_count, " tries.")
                success = True
    answer = input("Do you want to play again?")
    if answer.lower() == "yes":
        guessing_game()


guessing_game()

