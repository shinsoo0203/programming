sys.stdin = open("C:/input/주유소.txt", 'r')

n = int(input())
distance = list(map(int, input().split()))
oilstation = list(map(int, input().split()))

cost = 0
min = oilstation[0]

for i in range(n-1) :

    if oilstation[i] <= min :
        min = oilstation[i]
        cost += min * distance[i]
    elif oilstation[i] > min :
        cost += min * distance[i]
print(cost)