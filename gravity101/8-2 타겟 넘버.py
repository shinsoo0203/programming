from itertools import combinations

def FindingPossibleCase(numbers,answer,total_sum,target):
    for i in range(len(numbers)+1):
        for j in list(combinations(numbers, i)):
            if total_sum - sum(j)*2 == target:
                answer +=1

    return answer

def solution(numbers, target):
    answer = 0
    total_sum=sum(numbers)
    answer = FindingPossibleCase(numbers,answer,total_sum,target)
    return answer