import sys

if __name__ == '__main__':

    sys.stdin = open("C:/input/통계학.txt", 'r')

    n = int(input())
    tree = list(map(int, input().split()))
    tree = sorted(tree, reverse=True)

    current = 0
    count = 0

    for i in range(n) :
        if tree[i] >= current :
            current = tree[i]
            count += 2
        else :
            count += 1
            current -= 1

    print(current+count-1)