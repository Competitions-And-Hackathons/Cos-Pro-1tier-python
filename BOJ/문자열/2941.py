original_alphabat = input()
original_alphabat_length = len(original_alphabat)
answer = original_alphabat_length

alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in alphabets:
    for idx in range(original_alphabat_length - len(alphabet) + 1):
        substring = original_alphabat[idx:idx+len(alphabet)]

        if substring == alphabet:
            answer -= len(alphabet) - 1
            original_alphabat_list = list(original_alphabat)

            for substring_idx in range(len(alphabet)):
                original_alphabat_list[idx+substring_idx] = '*'

            original_alphabat = "".join(original_alphabat_list)

print(answer)