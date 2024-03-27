def coconut():
	height = input("Enter an integer between 1 and 5: ")
	#number=1
	#for loop used for rows
	if height.isdigit() and 0<int(height)<=5:
		height=int(height)
		for i in range(height):
			row=i+1
			print(" "*2*(height-row),end="") 
			for j in range(row,2*row):
				print(str(j)+" ",end="")
			print()
	else:
		print("That's not an integer between 1 and 5.")
	
	
	
	    
	    
	# number = 1       
	#		for j in range(i+1):
	#			print(j+1, end="")
	#		print(" " + "\n")
	# height+1)
		#for j in range(1, i+1):
			#print(number, end=" ")
			#number += 1
	    
	            
	
	
		
		
		
	
	
	
		
		
			
	
		
				
	
