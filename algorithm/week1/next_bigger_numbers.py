def binary(n):
    binary_list = []

    while True:
        a = int(n / 2)
        b = int(n % 2)
        binary_list.insert(0, b)
        if a != 0:
            n = a
        else:
            break
    return binary_list


def countOne(binary):
    count = 0
    for i in range(len(binary)):
        if binary[i] == 1:
            count += 1
    return count


def solution(n):

    if n > 1000000:
        return -1

    answer = 0

    next_number = n + 1
    while True:
        input_number_binary = binary(n)
        next_number_binary = binary(next_number)
        if countOne(input_number_binary) == countOne(next_number_binary):
            break
        next_number += 1

    answer = next_number
    return answer


solution(15)
