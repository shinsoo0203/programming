import heapq


def solution(scoville, K):
    answer = 0

    if K == 0:
        return 0

    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b * 2))
        answer += 1

    if scoville[0] < K:
        return -1
    return answer