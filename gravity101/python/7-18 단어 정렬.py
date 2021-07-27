import sys

sys.stdin = open("C:/input/카드정렬.txt", 'r')
n = int(input())

word = []

for _ in range(n):
    tmp_word = str(input())
    word_count = len(tmp_word)
    word.append((word_count, tmp_word))

word = list(set(word))

word = sorted(word, key=lambda x : (x[0], x[1]))

for i in range(len(word)):
    print(word[i][1])