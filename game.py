import random

list1 = [1,2,3,4,5,6,7,8,9,10]
guess_number = int(input("Guess a random number from 1 to 10: "))

if(random.choice(list1) == guess_number):
    print("You guessed it!")
else:
    print("You didn't guess it!")