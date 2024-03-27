def roomArea():
	q = float(input("Enter side A: "))
	w = float(input("Enter side B: "))
	e = float(input("Enter side C: "))
	r = float(input("Enter side D: "))
	t = float(input("Enter side E: "))
	area1 = q*w
	area2 = (q-e)*(r-t-w)
	area3 = 0.5*(q-e)*t
	print("Room Area: "+ str(area1+area2+area3))
