def odd():
	def is_odd_pow3(number):
		'''
		powr=3
		while powr<number: 
			powr*=9
		return number ==powr
	 '''
	
		if number <3:
			return False
		while number % 9==0:
			number//=9
		return number==3
	
			
			
		
	# You can modify these to test whether your function works
	print(is_odd_pow3(0)) # should print False
	print(is_odd_pow3(0.5)) # should print False
	print(is_odd_pow3(1)) # should print False
	print(is_odd_pow3(3)) # should print True
	print(is_odd_pow3(9)) # should print False
	print(is_odd_pow3(27)) # should print True
	print(is_odd_pow3(243)) # should print True
	print(is_odd_pow3(300)) # should print False
