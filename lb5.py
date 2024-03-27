def inputCheck():
	input_1 = input("Enter a 4-digit whole number: ")
	if len(input_1)==4 and (input_1).isdecimal() and input_1[0]!="0":
	  print("Thanks!")
	else:
	  print("That's not a 4-digit number.")
	
	
	input_2 = int(input("Enter an integer less than 50: "))
	if (input_2.isdecimal() or (input_2[1:].isdecimal and input_2[0]=="-")) and int(input_2) <50:
	  print("Thanks!")
	else :
	  print("That's not a number less than 50.")
	
	
	
	input_3 = input("Enter a string that begins with a vowel: " )
	if input_3[0].lower() in "aeiou":
	  print("Thanks!")
	else:
	  print("That does not begin with a vowel.")
	
	input_4 = input("Enter a string that ends with a consonant: ")
	if input_4[-1].isalpha() and input_4.lower()not in "aeiou": 
	  print("Thanks!")
	
	else:
	  print("That does not end with a constant.")