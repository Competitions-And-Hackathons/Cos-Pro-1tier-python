numbers = set()

for num in range(1, 10001):
    d_n = 0
    stringNum = str(num)
    for strNum in stringNum:
        d_n += int(strNum)
    d_n += num

    numbers.add(d_n)

all_numbers = set([i for i in range(1, 10001)])

self_numbers = all_numbers - numbers
self_numbers = sorted(list(self_numbers))
for self_number in self_numbers:
    print(self_number)