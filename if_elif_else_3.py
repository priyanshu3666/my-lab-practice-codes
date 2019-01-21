#program started
amount = int(input("Enter the amount of shopping by customer"))
if amount > 25000:
	discount = amount*0.20
	amount = amount - discount
	print("GOLD CUSTOMER \n the amount to be paid =",amount)
elif amount>10000 and amount<=25000:
	discount = amount*0.10
	amount = amount - discount
	print("SILVER CUSTOMER \n the amount to be paid =",amount)
else :
	discount = amount*0.05
	amount = amount - discount
	print("BRONZE CUSTOMER \n the amount to be paid =",amount)
#Program Ends
