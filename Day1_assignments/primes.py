def generate_primes(n):
    if n < 2:
        return "Not a prime number"
    else:
        primes = []
        for num in range(0,n+1):
            for i in range(2,num):
                if (num%i==0):
                    break
                else:
                    primes.append(num)
                    break
        return primes        
    print (primes)
