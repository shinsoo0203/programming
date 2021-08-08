def solution(priorities, location):
    queue = [[i, p] for i, p in enumerate(priorities)]

    answer = 0

    while len(queue) > 0:
        cur = queue.pop(0)

        max = cur[1]

        for i in range(len(queue)):
            if max <= queue[i][1]:
                max = queue[i][1]

        if max > cur[1]:
            queue.append(cur)
        else:
            answer += 1
            if location == cur[0]:
                return answer