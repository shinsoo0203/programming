def getParent(parent, x) :
    if parent[x] != x :
        parent[x] = getParent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

if __name__=="__main__" :
    answer = 0
    planet = list()
    n = int(input())
    for i in range(n):
        planet.append(list(map(int, input().split())))
    parent = [i for i in range(n)]
    x = []
    y = []
    z = []

    for i in range(n) :
        x.append([i, planet[i][0]])
        y.append([i, planet[i][1]])
        z.append([i, planet[i][2]])

    x = sorted(x, key = lambda a : a[1])
    y = sorted(y, key = lambda a : a[1])
    z = sorted(z, key = lambda a : a[1])

    node = []

    for i in range(n-1) :
        node.append([abs(x[i][1]-x[i+1][1]), x[i][0], x[i+1][0]])
        node.append([abs(y[i][1] - y[i + 1][1]), y[i][0], y[i + 1][0]])
        node.append([abs(z[i][1] - z[i + 1][1]), z[i][0], z[i + 1][0]])

    node.sort()
    res = 0

    for i in node :
        cost, a, b = i
        if getParent(parent, a) != getParent(parent, b) :
            union_parent(parent, a, b)
            answer += cost
            res += 1
        if res == n :
            break

    print(answer)