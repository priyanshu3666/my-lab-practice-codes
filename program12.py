#program started
#taking input
a = eval(input("Enter 1st side of triangle"))
b = eval(input("Enter 2nd side of triangle"))
c = eval(input("Enter 3rd side of triangle"))
if (a+b>c) and (b+c>a) and (a+c>b) :
	if (a == (b**2 + c**2)**0.5) or (b == (a**2 + c**2)**0.5) or (c == (b**2 + a**2)**0.5) :
		print("The triangle is Right Angle Triangle")
	elif (a == b) or (b == c) or (a == c) :
		print("The triangle is isoceles")
	else :
		print("the given triangle is scalene")
else :
	print("The given triangle is invalid")

#program ends
