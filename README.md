# hb-intro-final-project

# Final Project Name: Number Guessing Game

# Summary:
A number guessing game played from the command line against the computer. The player has 3 options for play: 
	
	1) Computer chooses number, player guesses
	2) Player chooses number, computer guesses
	3) Alternate between option 1 and option 2

# User Flow 

Opening the Program
Upon starting the program, the player will be informed of the game rules and will be prompted to choose an option to begin playing. 

Playing the Game
The player's experience will depend on the game selected: 

1) Computer chooses the number, player guesses
The player will have 6 attempts to guess the computer's number. Points earned by the player depends on the number of guesses made. Once a round is completed, the player will have the option to keep playing or switch to a different option for play. 

2) Player chooses number, computer guesses
The computer will have 6 attempts to guess the player's number. Points earned by the player depends on the number of guesses made by the computer. Once a round is completed, the player will have the option to keep playing or switch to a different option for play. 

3) Alternate between option 1 and option 2
This option will consist alternating between one round of option 1 and one round of option 2. The point structure will be the same as what is used in option 1 and option 2. Once a round is completed, the player will have the option to keep playing or switch to a different option for play. 

Points Structure 
There are 2 point structures, one which applies to option 1 and the second applies to option 2. 

1) Computer chooses number, player guesses
	- 1 guess:  100 points
	- 2 guesses: 50 points
	- 3 guesses: 30 points
	- 4 guesses: 15 points
	- 5 guesses: 10 points
	- 6 guesses: 05 points

2) Player chooses number, computer guesses
	- 6 guesses: 100 points
	- 5 guesses: 50 points
	- 4 guesses: 30 points
	- 3 guesses: 15 points
	- 2 guesses: 10 points
	- 1 guess:   05 points	

High Score List
The player's score will accumulate until player decides to exit the game. Upon exiting the game they will be able to enter their name, which will be stored in the list/dictionary with their name. 

# Potential Additional Feature
- Reward player with fun cat fact, maybe there is an API that can be used for this? 
- Ability to save player profile and keep continuous score
- Sassy computer comebacks for high or low scores

# Skills used
- Modules: Random module to generate a random number and time.sleep() to delay the computer's guess
- List: Used to keep count of the player's attempts
- Dictionary: Used to keep track of high scores and player profiles
- External files: Stores the dictionaries to be used as input when the game is played
- API (maybe): For cat facts

# Challenges

Structuring the Code
- Separate file for each of the game options? 
- How many files? 3 (1 for each game option), 1 shell file to call out to the 3 game files and save high score, 1 file to store the high score list, 1 file to store the cat fact api function that way it can be reused. 
 
Computer Guessing the number? 
- Can the random module be used? Is there a better module? 

High score list
- How do I store the high score dictionary from highest to lowest? Do I maybe need to use a list instead? 

Try and Except
- Need to get more familiar with how to use this

Cat facts api
- Is there a cat facts api? 
- If yes, how do I use it?

# Pseudocode

Shell File
print "Welcome. These are the rules of the game."
game_choice = raw input ("what option to you want to play?")

if game_choice = option1: 
	go to option 1 file
elif game_choice = option 2: 
	go to option 2 file
elif game_choice = option 3: 
	go to option 3 file 
elif game_choice = exit: 
	user_name = raw input ("enter the name you'd like save with your score.)
	score1 = {'user_name':'user_score'}

Game File 
print "Option 1 rules."
conditionals for option 1
call to the cat file api 

Cat file 
Function to pull cat fact from api