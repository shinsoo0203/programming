def solution(arr):
    arr.sort()
    answer = 0
    chk = False
    
    while chk is False :
        answer+= arr[-1]
        
        for i in range(len(arr)):
            if answer%arr[i]==0:
                chk=True
                #print(answer)
            else :
                chk=False
                break
    return answer
