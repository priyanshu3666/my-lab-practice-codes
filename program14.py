#program started
p_amt = eval(input("Enter principal amount"))
rate = eval(input("enter rate"))
time = eval(input("Enter time in year"))
compound_intrest = p_amt*((1+rate/100)**time)
print("The toal money after time given is ",compound_intrest)
#program ends
