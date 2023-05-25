def sequential_search_primes(data):
    primes = []
    for item in data:
        if is_prime(item):
            primes.append(item)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

my_list = [7, 10, 13, 6, 17, 22, 19]
prime_numbers = sequential_search_primes(my_list)
print("Bilangan prima dalam daftar adalah:", prime_numbers)
