def solution(dirs):
    answer = 0

    vector = {}

    x, y = 5, 5

    for i in range(len(dirs)):
        c = ''
        d = ''
        a, b = x, y

        if dirs[i] == 'U':
            if y < 10:
                y += 1
                x_y = [0, -1]
                a_b = [0, 1]
        elif dirs[i] == 'R':
            if x < 10:
                x += 1
                x_y = [-1, 0]
                a_b = [1, 0]
        elif dirs[i] == 'L':
            if x > 0:
                x -= 1
                a_b = [-1, 0]
                x_y = [1, 0]
        elif dirs[i] == 'D':
            if y > 0:
                y -= 1
                a_b = [0, -1]
                x_y = [0, 1]

        c += str(x)
        c += str(y)

        d += str(a)
        d += str(b)

        if c not in vector:
            vector[c] = [x_y]
            if d not in vector:
                vector[d] = [a_b]
            else:
                vector[d].append(a_b)
            answer += 1
        else:
            if x_y not in vector[c] :
                vector[c].append(x_y)
                vector[d].append(a_b)
                answer += 1

    return answer