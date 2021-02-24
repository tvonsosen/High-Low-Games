# Program where computer takes a random number and user guesses it

import random
#random function to take random number of range from 1 to 100
ran_num = random.randrange(1, 100)

guessed_num = input("""Guess a number between 1 and 100!
I will tell you when you are closer and further away from the number
as you keep guessing! """)
def num_game():
    '''number game for high low function, returns 1 for num_game to exit while loop later on'''
    global guessed_num
    if ran_num == int(guessed_num):
        print("Congratulations!!! You win!")
        return 1
    elif ran_num > int(guessed_num):
        guessed_num = input("Too low. Guess again! ")
        return 0
    elif ran_num < int(guessed_num):
        guessed_num = input("Too high. Guess again! ")
        return 0

guessedRight = 0
'''guessedRight is set equal to 0 and then set to the value of num_game in loop so that
when ran_num is guessed it can't go through the loop since not guessedRight is not 1 (which is 0)
and not true'''
while not guessedRight:
    guessedRight = num_game()
