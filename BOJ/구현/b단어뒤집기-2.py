input_S = input()

unflip_list = list()

unflip_start_index = None


for idx, s in enumerate(input_S):
    if s == '<':
        unflip_start_index = idx

    
    elif s == '>':
        unflip_list.append((unflip_start_index, idx))

        unflip_start_index = None


flip_list = list()
flip_start_index = 0

for unflip_index in unflip_list:
    flip_end_index = unflip_index[0]

    if flip_start_index + 1 < flip_end_index:
        flip_list.append((flip_start_index, flip_end_index))

    flip_start_index = unflip_index[1]

 

print(flip_list)