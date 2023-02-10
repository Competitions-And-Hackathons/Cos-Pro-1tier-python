from itertools import combinations

n = int(input())
right_solutions = input().split(' ')
answers = input().split(' ')

answer_list = list(combinations(right_solutions, 2))

total_grade = len(answer_list)
correct_grade = 0

for answer in answer_list:
    answer_indeces = answers.index(answer[0]) - answers.index(answer[1])
    solution_indeces = right_solutions.index(answer[0]) - right_solutions.index(answer[1])

    if answer_indeces * solution_indeces > 0:
        correct_grade += 1

print(str(correct_grade) + "/" + str(total_grade))