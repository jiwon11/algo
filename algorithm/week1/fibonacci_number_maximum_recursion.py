import sys
sys.setrecursionlimit(10**7)

fibonacci_dic = {0: 0, 1: 1}


def fibonacci(n):
    if n in fibonacci_dic.keys():
        return fibonacci_dic[n] % 1234567

    fibonacci_dic[n] = (fibonacci(n-1) % 1234567 +
                        fibonacci(n-2) % 1234567) % 1234567
    return fibonacci_dic[n] % 1234567


def solution(n):
    if n < 2:
        return -1
    if n > 100000:
        return -1

    answer = fibonacci(n)
    return answer


solution(20)
