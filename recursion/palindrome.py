# https://www.acmicpc.net/problem/25501

import sys

n = int(input())

def palindrome(left, right, word):
    if left >= right:
        return 1, 1
    elif word[left] == word[right]:
        isPalin, num = palindrome(left + 1, right - 1, word)
        return isPalin, num + 1
    else:
        return 0, 1

for _ in range(n):
    word = sys.stdin.readline().strip()
    isPalin, num = palindrome(0, len(word)-1, word)
    print(isPalin, num)