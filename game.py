import random

list1 = [1,2,3,4,5,6,7,8,9,10]
guess_number = int(input("Guess a random number from 1 to 10: "))

if(random.choice(list1) == guess_number):
    print("You guessed it!")
elif(random.choice(list1) != guess_number):
    if(random.choice(list1) < guess_number):
        print("Too high!")
    elif(random.choice(list1) > guess_number):
        print("Too low!")
    print("guess again")
    guess_number1 = int(input("Guess the number: "))
    if(random.choice(list1) == guess_number1):
        print("You guessed it!")
    else:
        print("You lost!, Try again")