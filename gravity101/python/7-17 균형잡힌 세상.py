import sys

sys.stdin = open("C:/input/카드정렬.txt", 'r')

while 1 :
    sentence = input().rstrip()
    stack = list()
    print(sentence)

    for i in sentence:
        if i == '(' :
            stack.append(i)
        elif i == ')' and len(stack) == 0 :
            stack.append(i)
        elif i == ')' and stack[-1] == '(' :
            stack.pop()

        if i == '[' :
            stack.append(i)
        elif i == ']' and len(stack) == 0 :
            stack.append(i)
        elif i == ']' and stack[-1] == '[' :
            stack.pop()


    if len(stack) > 0 :
        print("no")
    else :
        print("yes")
    if sentence == '.' :
        break