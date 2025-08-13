for number in range():
	dig1 = number / 10000;
	dig2 = number % 10000 / 1000;
	dig3 = number % 1000 / 100;
	dig4 = number % 100 / 10;
	dig5 = number % 10;
if number < 10000 | number > 99999:                  
	print("Please enter incorrect");
if dig1 == dig5:
	print(number , "is a palindrome");
elif dig2 == dig3:  
	print(number , "is a palindrome");
elif dig4 == dig2:
	print(number , "is a palindrome");
else:
	print(number , "not is a palindrome");
