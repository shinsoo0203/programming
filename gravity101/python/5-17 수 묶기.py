n = int(input())
num = []
for i in range(n) :
    num.append(int(input()))

num = sorted(num)


sum = 0

if n % 2 == 0 :
    for i in range(len(num)-1, 1, -2) :
        if num[i] * num[i-1] > 0:
            sum += num[i] * num[i-1]
        elif num[i] > 0 and num[i-1] < 0 :
            sum += num[i] + num[i-1]
        elif num[i] == 0 and num[i-1] < 0 :
            sum += num[i] * num[i-1]
else :
    for i in range(len(num) - 1, 0, -2) :
        if i == 0 :
            sum += num[i]
        if num[i] * num[i-1] > 0:
            sum += num[i] * num[i-1]
        elif num[i] > 0 and num[i-1] < 0 :
            sum += num[i] + num[i-1]
        elif num[i] == 0 and num[i-1] < 0 :
            sum += num[i] * num[i-1]

print(sum)