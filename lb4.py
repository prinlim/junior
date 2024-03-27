import random
"""
The function is defined as the passwordGenerator serves its purpose as a name given a collection of commands. 
The variable in the function act as the ingredients that give extra information, which will help us make a generated password. The random library is also called in the variable to give us random numbers, words, or characters for the final code. The newPassword is then created from the combination of the different variable  datatypes and a print statement, with integers made as strings. The function is ended with passwordGenerator(). 
"""
def egg():
	def passwordGen():
	    listofAnimals=["cat","dog", "racoon", "sheep", "crow","frog","capybara","dragon","eel","panda","hawk","cobra","reindeer"]
	    ani=random.choice(listofAnimals)
	    beginningNum=random.randint(1,100)
	    lastNum=random.randint(1,30)
	    listofChar=["#","*","@","&"]
	    char=random.choice(listofChar)
	    newPassword=str(beginningNum) + ani +str(lastNum) + char
	    print("Your new password is: ")
	    print(newPassword)
	passwordGen()
"""
The function defines the diceroll a serves its purpose as the name given to find the sides of the dice randomly rolled. roll1 and roll2 pull from the random library numbers 1 through 6, to represent the die, and is printed as strings in a print statement. The function is ended with diceroll(). 
"""
#def diceroll():
 #   roll1=random.randint(1,6)
  #  roll2=random.randint(1,6)
   # print("You've roll:")
   # print(str(roll1) + " and " + str(roll2))  
#diceroll()