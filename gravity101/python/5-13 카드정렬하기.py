import sys

result = 0
sys.stdin = open("C:/input/카드정렬.txt", 'r')
n = int(input())


card = list(int(input()) for i in range(n))
heapq.heapify(card)

while len(card) > 1:
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)
    sum = num1 + num2
    result += sum
    heapq.heappush(card, sum)

print(result)