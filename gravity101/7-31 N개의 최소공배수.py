from collections import Counter

def solution(arr):
    answer = 1

    count = {}

    for i in arr:
        j = 2
        check = []
        while i != 1:
            if i % j == 0:
                i = i // j
                check.append(j)
            else:
                j += 1

        c = Counter(check)

        for i in c:
            if i not in count:
                count[i] = c[i]
            elif c[i] > count[i]:
                count[i] = c[i]

    print(count)
    for i in count:
        if count[i] != 0:
            answer = (i ** count[i]) * answer

    return answer