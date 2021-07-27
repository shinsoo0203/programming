n = str(input())

prev = ''
count = 0
for i in range(len(n)) :
    if prev == '':
        pass
    elif n[i] != prev:
        count += 1
    prev = n[i]

print((count+1)//2)