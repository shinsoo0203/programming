def solution(lottos, win_nums):
    answer = []

    count = 0;
    zero_count = 0;
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1

        if lottos[i] == 0 or lottos[i] in win_nums:
            zero_count += 1

    if zero_count == 6:
        answer.append(1)
    elif zero_count == 5:
        answer.append(2)
    elif zero_count == 4:
        answer.append(3)
    elif zero_count == 3:
        answer.append(4)
    elif zero_count == 2:
        answer.append(5)
    else:
        answer.append(6)

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer