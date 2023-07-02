def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b % 1234567, a+b % 1234567
    return a % 1234567


def solution(n):
    if n < 2:
        return -1
    if n > 100000:
        return -1

    answer = fibonacci(n)
    return answer


solution(20)
