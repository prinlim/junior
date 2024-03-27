def leap():
	year = int(input("Enter a year: "))
	#leap year is a year that has an extra day in February. 
	# If you were born on February 29th, then you can only celebrate your birthday every four years on that date.
	#Every year, February ends on the 28th and every 4 years we have a leap year that makes February longer by a day
	if (year<=1752): #start of the Gregorian calendar
	  print("Leap years didn't exist back then!")
	# a tropical year is 265 days, 5 hours, 48 minutes, 45 seconds and 138 milliseconds
	# Every 4 years, make it leap is Julian Calendar
	# If the year is multiple of 100, it is not a leap year
	# If the year is a multiple of 400, it is a leap year
	# If the year is a multiple of 10,000 + 2800, it is not a leap year
	
	elif year>10000 and (year-2800)%10000== 0 and (year%100)==0:
		print(year, " is NOT a leap year")
	#if the year eands in 2800 or 5600 or 8400, THAT is not leap year
	elif year<10000 and (year-2800)%10000==0:
		print(year, " is NOT a leap year")
	elif year<10000 and (year-5600)%10000==0:
		print(year, " is NOT a leap year")
	elif year<10000 and (year-8400)%10000==0:
		print(year, " is NOT a leap year")
	else: # to tell what is a leap year
		if year%400==0:
			print(year, " is a LEAP year.")
		elif year%100!=0 and year%4==0:
			print(year, " is a LEAP year.")
		else:
			print(year, " is NOT a LEAP year")
		
	
	
	
