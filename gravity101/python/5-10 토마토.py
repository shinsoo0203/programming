import collections

n,m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))
queue = collections.deque([])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for x in range(m):
    for y in range(n):
        if graph[x][y] == 1:
            queue.append([x,y])
while queue:
    x,y = queue.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if -1 < new_x < m and -1 < new_y < n and graph[new_x][new_y] == 0:
            queue.append([new_x,new_y])
            graph[new_x][new_y] = graph[x][y] + 1
count = 0
for i in m :
    for j in n :
        if count < graph[i][j] :
            count = graph[i][j]
        if graph[i][j] == 0 :
            c = 1

if c == 1 :
	print(1)
else :
	print(count-1)