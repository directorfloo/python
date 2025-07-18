principal = int(input('Enter the principal amount'))
rate = int(input('Enter the rate of the loan'))
duration = int(input('Enter the duration of the loan'))
PERCENTAGE = 100
MONTH_IN_YEARS = 12
rate = rate / (PERCENTAGE * MONTH_IN_YEARS) 
duration = duration * MONTH_IN_YEARS

mortgage = principal * (rate * (1 + rate) ** duration) / ((1 + rate) ** duration - 1)
print ('Amount to pay for the morgage every month', mortgage)
