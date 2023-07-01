import math


def solution(n, a, b):
    answer = 0

    if (n % 2 != 0 and n < pow(2, 1) and n > pow(2, 20)):
        return -1

    if (a == b):
        return -1

    if (a > n):
        return -1

    if (b > n):
        return -1

    round = 1
    aGameIndex = math.ceil(a/2)
    bGameIndex = math.ceil(b/2)
    while aGameIndex != bGameIndex:
        aGameIndex -= aGameIndex // 2
        bGameIndex -= bGameIndex // 2
        round += 1
    answer = round
    return answer
