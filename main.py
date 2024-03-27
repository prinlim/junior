#this code lets the python labs and assignments be imported by there function names into this portfolio called main.py
from lb2 import change
from lb5 import inputCheck
from lb6 import leap
from lb7 import movie
from lb8 import coconut
from lb9 import odd
from lb4 import egg
from ps1 import silly
from ps2 import roomArea
from ps3 import grief
from ps4 import cup
from ps7 import calen
from ps8 import personal
from dn import cat

#This is going to be the way I pull other files on the filetree


#Welcome statement
print("Welcome to my Portfolio")
print("=============================")
print("=============================")
# for the labs options to print, the portfolio_state must be true
portfolio_state=True

# The while loop allows to print all labs since the portfolio_state is true, where the user can pick from 1-16
while portfolio_state==True:
	print("Labs: ")
	print("1. Smiley Face (TBD) ")
	print("2. Coin Calculator ")
	print("3. Talking Text (TBD)")
	print("4. Password Generator ")
	print("5. Input Checker ")
	print("6. Leap Year Check")
	print("7. Age-Related Conditions")
	print("8. Number Checker ")
	print("9. Odd Powers of Three")
	print("10. Pong (TBD)")
	print("11. Project Stem 1 - Silly Sentences")
	print("12. Project Stem 2 - Room Area")
	print("13. Project Stem 3 - Chatbot")
	print("14. Project Stem 4 - Divisible by Three")
	print("15. Project Stem 6 - Animation (TBD)")
	print("16. Project Stem 7 - Calendar")
	print("17. Project Stem 8 - Personal Organizer")
	print("18. DO NOW ASCII Cat or Penguin")


	lab_choice= input("Which lab or Project Stem assignment do you want to see? (1-17)? ")
	#The first lab is written as an if, then the rest of the finished labs are elifs
	if lab_choice=="2":
		change()
	elif lab_choice=="5":
		inputCheck()
	elif lab_choice=="4":
		egg()
	elif lab_choice=="6":
		leap()
	elif lab_choice=="7":
		movie()
	elif lab_choice=="8":
		coconut()
	elif lab_choice=="9":
		odd()
	elif lab_choice=="11":
		silly()
	elif lab_choice=="12":
		roomArea()
	elif lab_choice=="13":
		grief()
	elif lab_choice=="14":
		cup()
	elif lab_choice=="18":
		cat()
	elif lab_choice=="16":
		calen()
	elif lab_choice=="17":
		personal()
		print("Personal Organizer Executed")
	# for unfinished or non-functioning labs, it will output a print statement of being unavailable 
	elif lab_choice=="1" or lab_choice=="3" or lab_choice=="10" or lab_choice=="15":
		print("Currently unavaible due to simplegui or play package")
	
		
	#The else statement says to the user to print a valid number to see
	else:
		print("Choose a Valid Game")
	
	# After the first run of whatever lab the user picks, it asks the options to see more labs
	playAgain = input("Do you want to keep exploring my portfolio? (y/n): ")
	# An if statement is used for the portfolio_state code to play again. 
	if playAgain!="y":
		portfolio_state=False
		print("")
# for anything other than "y" that is inputted, it stops the portfolio_state function from outputting
print("Thanks for taking the time to look at my python programming work!")



