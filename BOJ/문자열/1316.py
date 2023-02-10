N = int(input())
answers = 0

strings = list()

for _  in range(N):
    strings.append(input())

for inputString in strings:
    alphabet_history = list()
    last_alphabet = ""
    is_group_word = True

    for inputStr in inputString:
        if last_alphabet != inputStr:
            if inputStr in alphabet_history:
                is_group_word = False
                last_alphabet = inputStr
                break
            else:
                alphabet_history.append(inputStr)
                last_alphabet = inputStr
    
    if is_group_word:
        answers += 1
        
print(answers)