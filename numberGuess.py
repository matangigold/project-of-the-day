import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

#Function to check users' guess
def check_answer(user_guess, actual_answer, turns):
    if user_guess < actual_answer:
        print("Too low.")
        return turns -1
    elif user_guess > actual_answer:
        print("Too high.")
        return turns -1
    else:
        print("You got it! The answer was %s" % (actual_answer))

#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    #number guessing game that prompts the user to guess a number between 1 and 100
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print("the correct answer is %s" % (answer))

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print("You have %s attemps remaining to guess the number." % (turns))
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses")
            return
        elif guess != answer:
            print("Guess again")
        

game()
