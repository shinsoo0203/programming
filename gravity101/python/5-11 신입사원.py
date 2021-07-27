sys.stdin = open("C:/input/신입사원.txt", 'r')

t = int(input())
for i in range(t):
    n = int(input())

    people = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(n)], key=lambda x: x[0])

    count = 1
    min = people[0][1]

    for j in range(1, n):
        if min > people[j][1] :
            min = people[j][1]
            count += 1
    print(count)