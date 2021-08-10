import math


def solution(s):
    answer = 0

    for x in range(len(s)):

        t = s[:x + 1]
        k = len(t)
        for y in range(len(t)):
            t = s[y:x + 1]

            check = True

            for i in range(len(t) // 2):
                if t[i] != t[-i - 1]:
                    check = False
                    break

            if check is True:
                if len(t) >= answer:
                    answer = len(t)
                    break

    return answer