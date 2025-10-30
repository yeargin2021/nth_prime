prime_numbers = []

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(0,10001):
    if is_prime(i)==True:
        #print(f"{i} is a prime number.")    
        prime_numbers.append(i)
# print(prime_numbers)

# print(prime_numbers[1000-1])


def nth_prime(n):
    n = prime_numbers[n-1]
    return n

nth_prime(5)
nth_prime(10)
nth_prime(16)
nth_prime(99)
nth_prime(1000)