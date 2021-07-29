def solution(p):
    answer = ''

    if len(p) == 0:
        return answer

    u = ''
    v = ''
    left, right = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    print(u, v)
    stack = []
    for i in range(len(u)):
        if not stack:
            stack.append(u[0])
        elif u[i] == '(':
            stack.append(u[i])
        elif stack[-1] == '(' and u[i] == ')':
            stack.pop()

    if not stack:
        answer += u
        answer += solution(v)

    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        u = u[1:-1]

        for t in range(len(u)):
            if u[t] == '(':
                answer += ')'
            else:
                answer += '('
    return answer


#1차     시도

# def solution(p):
#     answer = '
#
#
# while len(p) > 0:
#     stack = []
#     if p[0] == "(":
#         for i in range(len(p)):
#             if p[i] == '(':
#                 stack.append(p[i])
#             elif p[i] == ')':
#                 stack.pop()
#             if len(stack) == 0:
#                 answer += p[0:i + 1]
#                 if i == len(p) - 1:
#                     p = ''
#                 else:
#                     p = p[i + 1:]
#                 break
#     else:
#         left, right = 0, 0
#         for i in range(len(p)):
#             if p[i] == ')':
#                 left += 1
#             else:
#                 right += 1
#             if left == right:
#                 answer += '('
#
#                 for t in range(1, i):
#
#                     if p[t] == ')':
#                         answer += '('
#                     else:
#                         answer += ')'
#                 answer += ')'
#
#                 if i == len(p) - 1:
#                     p = ''
#                 else:
#                     p = p[i + 1:]
#                 break
# return answer



# 2차시
# def solution(p):
#     p = list(p)
#     answer = ''
#
#     while len(p) > 0:
#         u = []
#         v = []
#         left, right = 0, 0
#
#         for i in range(len(p)):
#             if p[i] == '(':
#                 left += 1
#             else:
#                 right += 1
#             if left == right:
#                 u = p[:i + 1]
#                 v = p[i + 1:]
#                 break
#         p = v
#         print(p)
#         stack = []
#         for i in range(len(u)):
#
#             if not stack:
#                 stack.append(u[0])
#             elif u[i] == '(':
#                 stack.append(u[i])
#             elif stack[-1] == '(' and u[i] == ')':
#                 stack.pop()
#
#         if not stack:
#             for i in u:
#                 answer += i
#         else:
#             u.pop(0)
#             u.pop(-1)
#
#             for t in range(len(u)):
#                 if u[t] == '(':
#                     u[t] = ')'
#                 else:
#                     u[t] = '('
#
#             answer += '('
#
#             for t in range(len(u)):
#                 answer += u[t]
#             answer += ')'
#
#     return answer