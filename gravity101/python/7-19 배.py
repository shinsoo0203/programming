import sys

sys.stdin = open("C:/input/카드정렬.txt", 'r')

n = int(input())
ship = list(map(int, input().split()))
m = int(input())
load = list(map(int, input().split()))

ship.sort(reverse = True)
load.sort(reverse = True)

answer = 0

if load[0] > ship[0] :
    print(-1)
else :
    while(len(load) > 0) :
        answer += 1
        for i in ship :
            for j in range(len(load)) :
                if i >= load[j] :
                    del load[j]
                    break
    print(answer)
