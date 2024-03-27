def calen():
	def leap_year(y):
	    if (y % 400 == 0) and (y % 100 == 0):
	        return 1
	    elif (y % 4 == 0) and (y% 100!=0):
	        return 1
	    else :
	        return 0
	
	def number_of_days(m, y):
	    y = leap_year(y)
	    if m ==1 or m== 3 or m==5 or m==7 or m==8 or m==10 or m==12:
	        return 31
	    elif m==4 or m==6 or m==9 or m==11:
	        return 30
	    elif m == 2:
	        if leap_year(y) == 1:
	            return 29
	        elif y==0:
	            return 28
	 
	
	
	def days_passed(d, m, y):
	    passed = 0
	   
	    for i in range(1, m):
	        passed = (number_of_days(i, d) + passed)
	    return (passed + d - 1)
	
	
	
	print("Please enter a date")
	d = int(input("Day: "))
	m = int(input("Month: "))
	y = int(input("Year: "))
	
	
	print("Menu:")
	print("1) Calculate the number of days in the given month.")
	print("2) Calculate the number of days passed in the given year.")
	
	menu = int(input())
	
	if menu == 1:
	    print(number_of_days(m, y))
	
	elif menu == 2:
	    print(days_passed(d, m, y))
	
	
	else :
	    print("Invalid choice.")