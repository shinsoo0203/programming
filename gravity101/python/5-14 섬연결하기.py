from collections import deque


def solution(n, costs):
    answer = 0
    nodes = {}
    costs.sort(key=lambda x: x[2])

    path = [costs[0][0]]
    print(costs)
    while len(path) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in path) and (cost[1] in path):
                continue
            elif (cost[0] in path) or (cost[1] in path):
                answer += cost[2]
                path.append(cost[0])
                path.append(cost[1])
                path = list(set(path))
                costs.pop(i)
                break
    return answer