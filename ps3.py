import random 
def grief():
	listoflikes =["Wow, awesome stuff!", "Woah, that's quite intersting.", "Aye, that's pretty dope.", "That's quite a nice style you got there!"]
	flop = random.choice(listoflikes)
	name = input("What is your first name?")
	print(name)
	
	shoes = input("What is your favorite type of shoes? ")
	print(shoes)
	if shoes=="sneakers":
	    print("Nice, casual style.")
	elif shoes=="loafers":
	    print("Cool, nice and formal style.")
	elif shoes=="heels":
	    print("Great style! Elegant and confident.")
	else:
	    print("Nice, superb taste in shoes!")
	
	age = int(input("How old are you?"))
	print(age)
	print(str(age) + " is a good age to invest in fashion.")
	
	acc = input("What is your favorite type of accessory?")
	if acc =="rings":
	    print(flop)
	elif acc=="necklaces":
	    print(flop)
	elif acc=="bracelet":
	    print(flop)
	else:
	    print(flop)
	print("Let's keep this converstation going!")
	
	shirt = input("What is your favorite type of shirt? ")
	if shirt== "graphic tees":
	    print("That's pretty cool, you could style that will alotta things.")
	elif shirt=="dress shirts":
	    print("Oo, how elegant with a formal, chic style. ")
	elif shirt=="button-up":
	    print("Oo, how elegant with a formal, chic style. ")
	else:
	    print("Wah, your fashion sense never fails to disappoint.")
	
	more = input("Well our time is up, anything else you like to add")
	print(more)
	print("Well " + name + " I loved hearing about your fashion sense.")



