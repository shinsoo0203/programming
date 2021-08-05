import sys
import collections

sys.stdin = open("C:/input/카드정렬.txt", 'r')
n = int(input())
graph = []
for _ in range(n+1):
    graph.append([0 for _ in range(n+1)])
num = int(input())
for _ in range(num):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
print(graph)
infected = 1
q = collections.deque([])
q.append(infected)
visited = [False for _ in range(n+1)]

while len(q) != 0:
    p = q.pop()
    visited[p] = True
    for i in range(1,n+1):
        if graph[p][i] == 1 and visited[i] == False:
            q.append(i)

print(sum(visited)-1)

# n = int(input())
# m = int(input())
#
# node = {}
#
# for i in range(n) :
#     node[i+1] = []
#
# for i in range(m) :
#     x, y = map(int, input().split())
#     node[x].append(y)
#     node[y].append(x)
#
# visited = []
#
# stack = []
# stack.append(1)
#
# visited.append(1)
#
# while len(stack) > 0 :
#     t = stack.pop()
#
#
#     for i in node[t] :
#             if i not in visited :
#                 stack.append(i)
#                 visited.append(i)
#
#
# print(len(visited)-1)