def solution(scoville, K):
    answer = 0
    old=0
    
    while True:
        
        scoville.sort()
        
        if scoville[0]>=K: return answer
        elif len(scoville)>1:
            scoville[0]+=scoville[1]*2
            scoville[1:]=scoville[2:]
            answer += 1
            new = scoville[0]
        else: return -1
        if old==scoville[0]: return -1
    return answer
