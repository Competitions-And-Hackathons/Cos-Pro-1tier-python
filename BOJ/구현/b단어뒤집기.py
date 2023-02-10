input_S = input()

flip_list = list()

flip_start_index = None
is_flipped = False

for idx, s in enumerate(input_S):
    if s == '<':
        flip_start_index = idx
        is_flipped = True
    
    elif s == '>':
        flip_list.append((flip_start_index, idx))

        flip_start_index = None
        is_flipped = False

print(flip_list)

for flip_info in flip_list:
    flipped_substring = input_S[flip_info[0]+1 : flip_info[1]]
    flipped_substring = flipped_substring[::-1]

    flip_start_index = flip_info[0] + 1

    for flip_indx, sub in enumerate(flipped_substring):
        input_S = input_S[:flip_start_index + flip_indx] + sub + input_S[flip_start_index + flip_indx + 1 : ] 

print(input_S)