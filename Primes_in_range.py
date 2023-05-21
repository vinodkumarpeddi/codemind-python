def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
a = int(input())
b = int(input())
primes = []
for i in range(a, b+1):
    if is_prime(i):
        primes.append(i)
print(len(primes))