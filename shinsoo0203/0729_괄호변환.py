def solution(p):
    answer = ''

    if p=='': return ''
    u, v = isbalance(p)
    
    if isright(u):
        answer= u+solution(v)
    else:
        answer='('+solution(v)+')'
        #print(answer)
        for i in range(1,len(u)-1):
            if u[i]=='(': answer+=')'
            else: answer+='('
    return answer

def isbalance(p):
    u, v ='',''
    bal = 0
    for i in range(len(p)):      
        if p[i]=='(': bal += 1
        else :        bal -= 1
            
        if bal==0:
            u = p[0:i+1]
            v = p[i+1:]
            break
    #print(u)
    #print(v)
    return u,v

def isright(p):
    bal =0
    for i in range(len(p)):
        if p[i]=='(': bal+=1
        elif bal>0: bal-=1
        else: return False
    return True
