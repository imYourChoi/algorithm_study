# https://www.acmicpc.net/problem/1062

from itertools import combinations


def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit


N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]
bits = list(map(word2bit, words))
base_bit = word2bit('antic')

if K < 5:
    print(0)
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    answer = 0
    for combination in combinations(alphabet, K-5):
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits:
            if bit & know_bit == bit:
                count += 1
        answer = max(answer, count)
    print(answer)
