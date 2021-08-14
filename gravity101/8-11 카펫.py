def solution(brown, red):
    for y in range(brown):
        for x in range(y, brown):

            if x * y == brown + red and (x - 2) * (y - 2) == red:
                return x, y