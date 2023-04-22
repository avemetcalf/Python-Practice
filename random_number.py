import random

#Defined variable guess between 1 and x
def guess(x):
    random_num = random.randint(1, x)
    
    guess = 0
    
    #While you guessed incorrectly the loop will print out these statements
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Sorry, guess again. Too low!")
        elif guess > random_num:
            print("sorry, guess again: Too high!")

    #Guessed number correctly print statement
    print(f"Congrats you guessed {random_num} correctly!")

#End parameter for guessing number
guess(10)