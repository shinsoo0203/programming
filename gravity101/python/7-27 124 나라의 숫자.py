def solution(n):
    list = [1, 2, 4]
    answer = ''
    while n > 0:
        n -= 1
        answer = str(list[n % 3]) + answer
        n //= 3
    return answer