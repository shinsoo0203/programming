def solution(genres, plays):
    answer = []
    genresdic = {}
    genrank = {}

    for i in genres:
        genresdic[i] = [0]
        genrank[i] = 0

    for i in range(len(genres)):

        temp2 = plays[i]
        temp2 += genrank[genres[i]]
        genrank[genres[i]] = temp2

        if genresdic[genres[i]] == [0]:
            genresdic[genres[i]] = [plays[i]]
        else:
            if len(genresdic[genres[i]]) == 1:
                if genresdic[genres[i]][0] > plays[i]:
                    temp = genresdic[genres[i]]
                    temp.append(plays[i])
                    genresdic[genres[i]] = temp

                else:
                    temp = [plays[i]]
                    temp += genresdic[genres[i]]
                    genresdic[genres[i]] = temp
            else:
                if genresdic[genres[i]][0] < plays[i]:
                    genresdic[genres[i]][1] = genresdic[genres[i]][0]
                    genresdic[genres[i]][0] = plays[i]
                elif genresdic[genres[i]][1] < plays[i]:
                    genresdic[genres[i]][1] = plays[i]

    genrank = sorted(genrank, key=lambda x: genrank[x], reverse=True)

    for i in genrank:
        for j in genresdic[i]:
            answer.append(plays.index(j))
            plays[plays.index(j)] = 0
    return answer