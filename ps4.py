def cup():
	n = int(input("How many numbers do you need to check? "))
	d = 0
	o = 0
	
	for i in range(n):
	    num=int(input("Enter number "))
	    if num %3 == 0:
	        d +=1
	        print(str(num) + " is divisible by 3.")
	    else:
	        o+=1
	        print(str(num) + " is not divisible by 3.")
	print("You entered " + str(d) + " number(s) that are divisible by 3.")
	print("You entered " + str(o) + " number(s) that are not divisible by 3.")
