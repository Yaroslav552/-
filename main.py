numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i < 2:
        not_primes.append(i)
        continue

    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(f'Простые числа: {primes}')
print(f'Непростые числа: {not_primes}')
