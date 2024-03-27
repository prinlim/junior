def change():
	num_pennies = int(input("Enter the number of pennies: "))
	num_nickels = int(input("Enter the number of nickels: "))
	num_dimes = int(input("Enter the number of dimes: "))
	num_quarters = int(input("Enter the number of quarters: "))
	num_loonies = int(input("Enter the number of loonies: "))
	num_toonies = int(input("Enter the number of toonies: "))
	
	print("Number of pennies:", num_pennies)
	print("Number of nickels:", num_nickels)
	print("Number of dimes:", num_dimes)
	print("Number of quarters:", num_quarters)
	print("Number of loonies:", num_loonies)
	print("Number of toonies:", num_toonies)
	
	total_value= (num_pennies + 5*num_nickels+10*num_dimes+25*num_quarters+100*num_loonies+ 200*num_toonies)/100
	
	print("Total value of coins: $" + "{:.2f}".format(total_value))
	
	total_value= (num_pennies + 5*num_nickels+10*num_dimes+25*num_quarters+100*num_loonies+ 200*num_toonies)/100
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#a = int(num_pennies) * 0.01
	#b = int(num_nickels) * 0.05
	#c = int(num_dimes)  * 0.10
	#d = int(num_quarters) * 0.25
	#e = int(num_loonies) * 1
	#f = int(num_toonies) * 2
	# $1, loonie = 100c
	# $2, toonie = 200c
	
	#total_value= a + b + c + d + e + f