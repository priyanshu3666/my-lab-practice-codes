def delete(list): 
	final= []
	dupli=[]
	for num in list: 
		if num not in final: 
			final.append(num)
		else:
                        dupli.append(num)
	return final,dupli
list = [2,4,10,20,5,2,20,4,4] 
print(delete(list)) 

