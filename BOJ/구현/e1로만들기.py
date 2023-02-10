from collections import deque

input_int = int(input())

queue = deque([(input_int, 0)])

number_dict = dict()
number_dict[input_int] = 0

while queue:
    node = queue.popleft()

    current_key = node[0]
    current_calculation = node[1]
    calculated_number = current_calculation + 1


    if current_key % 3 == 0:
        threed_key = current_key//3
        if threed_key > 0:
            if threed_key in list(number_dict.keys()):
                if calculated_number < number_dict[threed_key] :
                    queue.append((threed_key, calculated_number))
                    number_dict[threed_key] = calculated_number
            else:
                queue.append((threed_key, calculated_number))
                number_dict[threed_key] = calculated_number

    if current_key % 2 == 0:
        twoed_key = current_key//2
        if twoed_key > 0:
            if twoed_key in list(number_dict.keys()):
                if calculated_number < number_dict[twoed_key] :
                    queue.append((twoed_key, calculated_number))
                    number_dict[twoed_key] = calculated_number
            else:
                queue.append((twoed_key, calculated_number))
                number_dict[twoed_key] = calculated_number


    oned_key = current_key - 1
    if oned_key > 0:
        if oned_key in list(number_dict.keys()):
            if calculated_number < number_dict[oned_key] :
                queue.append((oned_key, calculated_number))
                number_dict[oned_key] = calculated_number
        else:
            queue.append((oned_key, calculated_number))
            number_dict[oned_key] = calculated_number


print(number_dict[1])