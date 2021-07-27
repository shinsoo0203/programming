def solution(name):
    answer = 0
    count = 0
    acount = 0
    for i in name:

        if ord(i) - ord('A') < 13:
            count += ord(i) - ord('A')

        else:
            count += ord('Z') - ord(i) + 1

    for i in range(1, len(name)):
        if name[i] == 'A':
            acount += 1
        else:
            break

    return count + len(name) - 1 - acount