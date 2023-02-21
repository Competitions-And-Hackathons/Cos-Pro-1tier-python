from itertools import permutations

n = int(input())

total_count = 0

for bondeaged_count in range(n//2 + 1):
    one_count = n - 2*bondeaged_count

    square_list = [1]*one_count + [2]*bondeaged_count
    
    permutation_list = permutations(square_list)
    #print(set(permutation_list))
    
    if bondeaged_count == 0:
        total_count += 1

    else:
        total_count += len(set(permutation_list)) * (2 ** bondeaged_count)

print(total_count%10007)