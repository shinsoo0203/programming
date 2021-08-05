def solution(progresses, speeds):
    stack = []
    day = 1
    count = 1
    current_day = 0

    for i in range(len(progresses)):

        while progresses[i] + (speeds[i] * day) < 100:
            day += 1

        if len(stack) == 0:
            stack.append(count)
            current_day = day
        elif current_day == day:
            count += 1
            stack[-1] = count
        elif current_day != day:
            count = 1
            stack.append(count)
            current_day = day

    return stack