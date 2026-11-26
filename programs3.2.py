total = 0
for num in range(2, 200):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total = total + num
print("Sum of primes below 200 =", total)
