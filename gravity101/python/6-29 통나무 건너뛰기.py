import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sys.stdin = open("C:/input/통계학.txt", 'r')

    n = int(input())

    for i in range(n) :
        t = int(input())
        data = list(map(int, input().split()))
        data.sort()
        result = 0
        for j in range(2, N)
            result=max(result, abs(data[j]-data[j-2]))
        print(result)