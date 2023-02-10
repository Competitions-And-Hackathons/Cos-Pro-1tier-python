han_num_count = 0

N = int(input())
for i in range(1, N+1):
    if i < 100:
        han_num_count += 1

    elif i >= 100 and i <1000:
        c = i%10
        i //= 10
        b = i%10
        i //= 10
        a = i

        a_b = a-b
        b_c = b-c
        if a_b == b_c:
            han_num_count += 1
print(han_num_count)