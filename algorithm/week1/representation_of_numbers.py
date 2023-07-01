def solution(n):
    answer = 0
    if (n > 10000):
        return -1

    if (n < 0):
        return -1

    number = 1
    start_number = 1
    i = 1
    sum = 0
    while start_number <= n/2:
        sum += i
        if (sum == n):
            sum = 0
            start_number += 1
            i = start_number
            number += 1
        if (sum > n):
            sum = 0
            start_number += 1
            i = start_number
        i += 1

    answer = number
    return answer
