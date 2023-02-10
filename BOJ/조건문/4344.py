N = int(input())

strings = list()

for idx in range(N):
    strings.append(input())

for idx in range(N):
    inputString = strings[idx]
    student_num = int(inputString.split()[0])
    grades = inputString.split()
    del grades[0]

    grades = list(map(int, grades))
    avg = sum(grades)/student_num
    better_grades = list(filter(lambda x: x > avg, grades))

    output = str(round(len(better_grades)/student_num*100000))
    print(output[0:2] + "." + output[2:5]+ "%")