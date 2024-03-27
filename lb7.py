def movie():
	age = int(input("Enter your age: "))
	if age>=18:
		print("You can vote, get a driver's license, and watch all rated movies.")
	elif age>=85:
		print("You can vote, watch all rated movies, but you should take it easy when it comes to driving.")
	if age==17:
		print("You cannot vote yet, can watch all rated movies, and you can get a driving permit.")
	elif age==16:
		print("You cannot vote yet, can watch all movies except R-Rated ones, and you can get a driving permit.")
	else:
	 if age<16 and age>=13:
	   print("You are cannot to drive, cannot vote, and cannot watch R-Rated movies but can watch PG-13 movies and under, with adult supervision.")
	 elif age<13:
	  print("You are unable to vote, cannot drive, and cannot watch PG-13 movies and R-Rated movies but can watch G-Rated movies with parental guidance.")
		
	
		