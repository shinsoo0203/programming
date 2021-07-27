def solution(citations):

citations.sort()

length = len(citations)

for i in range(length, 0, -1):
    if citations[i-1] <= length-i:
        return length-i
return 0