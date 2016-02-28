
import random # module to generate random num
guess_list = [] # empty list to capture unique num of guesses
num_of_guesses = 0 # variable to track the num of guesses
correct_number = random.randint(1,100) # generate random num, save to variable 
end_game = False # flag to end the game when user guesses correct num 
winner = False
print correct_number

print 
print "*****************************************************"
print "*                                                   *"
print "*          WELCOME TO THE GUESSING GAME             *"
print "*    I am thinking of a number between 1 - 100      *"
print "*  You have 6 tries to guess my number, good luck!  *" 
print "*                                                   *"
print "*****************************************************\n"


while end_game == False and num_of_guesses < 6: # while loop to continue until user has made 6 guesses 
    try:
        guess = int(raw_input ("Enter your guess:     ")) # try casting guess as int

    except ValueError:
        print "Sorry, your guess is invalid because it is not a whole number.\n"  # prevents invalid characters from being entered
        continue 

    if int(guess) > 100: 
        print "Sorry, your guess is invalid because it is higher than 100.\n" # prevents nums greater than 100 from being entered
        end_game = False

    elif int(guess) < 0: 
        print "Sorry, your guess is invalid because it is lower than 1.\n" # prevents nums less than 1 from being entered
        end_game = False  

    else: # perform if guess is valid       

        if guess in guess_list: # number previously guessed 
            if int(guess) > correct_number: # too high 
                print "You already guessed %i, it is too high!\n" %(guess)
                num_of_guesses +=1
                end_game = False
            if int(guess) < correct_number: # too low
                print "You already guessed %i, it is too low!\n" %(guess)
                num_of_guesses +=1
                end_game = False    

        if guess not in guess_list: # first time num is guessed
            if int(guess) == correct_number: # guess is correct, end game
                guess_list.append(guess)
                num_of_guesses +=1
                print 
                print "*******************************"
                print "*          CORRECT!           *"
                print "*      The number was %i!     *" %(correct_number)
                print "*    It took you %i guesses!  *" %(num_of_guesses)
                print "*          YOU WIN!           *"
                print "*******************************\n"
                winner = True
                end_game = True   

            if int(guess) > correct_number: # too high 
                guess_list.append(guess)
                num_of_guesses +=1
                print "%i is too high, guess again.\n" %(guess)
                end_game = False

            if int(guess) < correct_number: # too low
                guess_list.append(guess)
                num_of_guesses +=1
                print "%i is too low, guess again.\n" %(guess)
                end_game = False


if winner == True: 
  print

else: 
    print 
    print "********************************"
    print "*          GAME OVER!          *"
    print "*      The number was %i!      *" %(correct_number)
    print "*          YOU LOSE!           *"
    print "********************************\n"


        

 