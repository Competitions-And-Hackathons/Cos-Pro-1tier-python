M = int(input())
N = int(input())


prime_numbers = list()

for number in range(M, N + 1):
    if number > 1:
        is_prime = True

        for small_number in range(2, number):
            if number % small_number == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_numbers.append(number)

if len(prime_numbers) > 0:
    print(sum(prime_numbers))
    print(min(prime_numbers))

else:
    print(-1)