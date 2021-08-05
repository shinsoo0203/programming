def solution(max_weight, specs, names):
    answer = 0

    sum_truck = 0
    dict = {}

    for i in range(len(specs)):
        dict[specs[i][0]] = specs[i][1]

    for i in range(len(names)):
        sum_truck += int(dict[names[i]])
        if sum_truck > max_weight:
            sum_truck = 0
            answer += 1
            sum_truck += int(dict[names[i]])

            return answer + 1