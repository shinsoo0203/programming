def solution(n):
    answer = ''
    rule='124'
    
    while n>0:
        n-=1
        answer=rule[n%3]+answer
        n//=3
        
    return answer
