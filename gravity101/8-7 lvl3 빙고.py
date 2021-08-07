def solution(board, nums):
    answer = 0
    bingo = [[False for i in range(len(board[0]))] for j in range(len(board[0]))]

    dic = {}

for i in range(len(board)):
    for j in range(len(board)):
        dic[board[i][j]] = [i, j]

for i in nums:
    x, y = dic[i]
    bingo[x][y] = True

    cross_right = True
cross_left = True
for i in range(len(bingo)):
    count_col = True
    count_row = True
    for j in range(len(bingo)):

        # row 체크
        if bingo[i][j] == False:
            count_col = False
        # col 체크
        if bingo[j][i] == False:
            count_row = False
        # cross_right 체크
        if j == i and bingo[i][j] == False:
            cross_right = False
            # cross_left 체크
            if bingo[i][len(bingo) - i - 1] == False:
    cross_left = False
    if count_col == True:
answer += 1
if count_row == True:
    answer += 1

if cross_right == True:
    answer += 1
if cross_left == True:
    answer += 1

return answer