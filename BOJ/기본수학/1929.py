input_numbers = list(map(int, input().split()))


prime_numbers = list()

for number in range(input_numbers[0], input_numbers[1] + 1):
    if number > 1:
        is_prime = True

        for small_number in range(2, number):
            if number % small_number == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_numbers.append(number)

prime_numbers = sorted(prime_numbers)
for prime_number in prime_numbers:
    print(prime_number)