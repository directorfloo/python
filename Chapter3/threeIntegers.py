number1 = int(input("Enter Integer"))
sum = number1
product = number1
smallest = number1
largest = number1
average = 0;
for count in range (3):
		number = int(input("Enter Integer"))
		sum += number
		product *= number
		average = sum / 3
		if largest > number:
	       		Largest = number
		if smallest < number:
			smallest = number
    
print(sum) 
print(product)
print(largest)
print(smallest) 
