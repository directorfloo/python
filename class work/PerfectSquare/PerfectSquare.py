import math
def   get_perfect_square(numbers):


	square_list = []
	for number in numbers:	
		if type(number) == float:
			raise ValueError
		if int(number) < 0:
			raise ValueError
		if type(number) == str:
			raise ValueError

		result = math.isqrt(number)
		if result * result == number:
			square_list.append(True)
		else:
			square_list.append(False)

	return square_list


get_perfect_squared = ([2, 3, 4, 9, 6, 25])
print(get_perfect_square(get_perfect_squared))


	



