from itertools import combinations
from collections import Counter


def solution(clothes):
    answer = 0

    dic = {}
    counter_each_category = Counter([cat for _, cat in clothes])

    print(counter_each_category)
    all_possible = 1
    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)
        print(counter_each_category[key])

    for i in range(len(clothes)):

        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = [clothes[i][0]]
        else:
            dic[clothes[i][1]].append(clothes[i][0])

    check = []

    for i in range(len(dic)):
        check.append(len(dic[clothes[i][1]]))

    for i in range(len(check)):
        result = []
        for j in check[i + 1:]:
            result.append((check[i], j))
        t = 1
        for i in result:
            for j in i:
                t *= j
        answer += t

    return all_possible - 1