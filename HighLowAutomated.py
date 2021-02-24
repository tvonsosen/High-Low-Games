# Program where computer guesses a number you come up with between 1 and 100

answer = input("Type a random number between 1 and 100 and I'm gonna try to guess it: ")
#guess is set to middle of 100 and 1, 100 for too low of a guess, 1 for too_high
guess = 50
too_high = 1
too_low = 101
#loop to guess the number and then see if it is too high or too low or if it is correct
while True:
    print("Is it " + str(guess) + "? ")
    next_option = input("""Type 1, 2, or 3, to tell me if I am right or how I should adjust my guess.
1. Too high
2. Too low.
3. You got it!!!\n""")
    if int(next_option) == 1:
        guess = (guess + too_high)//2
        too_low = (too_low+too_high)//2   
#loop so that if the guess is too high it takes the
#middle of it and too_high(initially set to 1) too_low is set to the average of it and too_high to adjust
    elif int(next_option) == 2:
        guess = (guess+too_low)//2
        too_high = (too_high+too_low)//2    
#loop so that if the guess is too too_low it takes the
#middle of it and too_low(initially set to 100) too_high is set to the average of it and the too_low to adjust
    else:
#loop to congratulate or start new game or check if I guessed correct answer
        if guess != int(answer):
            print("""That wasn't the number you inputed at first to be the answer!
Try again!""")
        else:    
            print("Yesss! Good game!")
            new_game = input("""Would you like to play again? Type the number corresponding to yes or no.
1. Yes
2. No\n""")
            if int(new_game) == 1:
                guess = 50
                too_high = 1
                too_low = 100
                answer = input("Think of a random number between 1 and 100 and I'm gonna try to guess it: ")
            else:
                print ("OK")
                break
        
