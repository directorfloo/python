def sieve(limit=1000):
    
    primes = [True] * limit

 
    primes[0] = primes[1] = False

   
    import math
    for num in range(2, int(math.sqrt(limit)) + 1):
        if primes[num]:
            # mark multiples of num as False
            for multiple in range(num * num, limit, num):
                primes[multiple] = False

   
    return [i for i, is_prime in enumerate(primes) if is_prime]



prime_numbers = sieve(1000)
print(prime_numbers)
