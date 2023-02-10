def find_prime(N):
    prime_numbers = list()

    for number in range(N + 1, 2*N + 1):
        if number > 1:
            is_prime = True

            for small_number in range(2, number):
                if number % small_number == 0:
                    is_prime = False
                    break
            
            if is_prime:
                prime_numbers.append(number)

    return len(prime_numbers) 


numbers = list()

while True:
    number = int(input())
    if number == 0:
        break

    numbers.append(number)

for number in numbers:
    print(find_prime(number))