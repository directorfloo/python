def get_addition(list):
	result =[]
	if list == 0:
		raise ValueError("invalid");
	if type(list) == str:
		raise ValueError("invalid");
	result.append(sum(list))
	return result



input : [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]
print(get_addition(input))






def get_addition(list):
	result =[]
	if list == 0:
		raise ValueError("invalid");
	if type(list) == str:
		raise ValueError("invalid");
	result.append(sum(list))
	return result



input : [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]
print(get_addition(input))