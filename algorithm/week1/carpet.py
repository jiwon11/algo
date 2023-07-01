def solution(brown, yellow):
    answer = []

    if (brown < 8 and brown > 5000):
        return -1

    if (yellow < 1 and yellow > 2000000):
        return -1

    total = brown + yellow

    for w in range(1, total):
        for h in range(1, w+1):
            if (w * h == total):
                if ((w-2) * (h-2) == yellow):
                    answer.append(w)
                    answer.append(h)
                    break
        if (len(answer) == 2):
            break
    return answer
