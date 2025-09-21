def number_to_words(n):
    ones = {
        0: "", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
        5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
    }
    teens = {
        10: "TEN", 11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN", 14: "FOURTEEN",
        15: "FIFTEEN", 16: "SIXTEEN", 17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN"
    }
    tens = {
        2: "TWENTY", 3: "THIRTY", 4: "FORTY", 5: "FIFTY",
        6: "SIXTY", 7: "SEVENTY", 8: "EIGHTY", 9: "NINETY"
    }

    words = ""

 
    if n >= 100:
        words += ones[n // 100] + " HUNDRED"
        n %= 100
        if n > 0:
            words += " "

    # Tens and ones
    if 10 <= n <= 19:
        words += teens[n]
    else:
        if n >= 20:
            words += tens[n // 10]
            n %= 10
            if n > 0:
                words += " " + ones[n]
        elif n > 0:
            words += ones[n]

    return words.strip()


def check_amount(amount):
    
    dollars = int(amount)
    cents = round((amount - dollars) * 100)
     dollar_words = number_to_words(dollars)   
    return f"{dollar_words} AND {cents:02d}/100"



print(check_amount(112.43))   
print(check_amount(50.05))    
print(check_amount(7.99))    
print(check_amount(300.00))   
