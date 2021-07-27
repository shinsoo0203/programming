n = int(input())
arrow_p = list(map(int, input().split()))
number = 0
count = 0
t = 0
for i in arrow_p :

    if i > t :
        t = i
        count = 0
    else :
        count += 1
    number = max(number, count)

print(number)