N = int(input())
numbers = list(map(int, input().split()))

maximum_number = max(numbers)
prime_numbers = list()

for number in range(2, maximum_number+1):
    is_prime = True

    for small_number in range(2, number):
        if number % small_number == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_numbers.append(number)


primes = 0

for number in numbers:
    if number in prime_numbers:
        primes += 1

print(primes)