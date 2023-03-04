# https://www.acmicpc.net/problem/1208

from itertools import combinations
from bisect import bisect_left, bisect_right

def getCount(seq, target):
    return bisect_right(seq, target) - bisect_left(seq, target)

def getSum(seq, sumSeq):
    for i in range(1, len(seq) + 1):
        for comb in combinations(seq, i):
            sumSeq.append(sum(comb))
    sumSeq.sort()

N,S = map(int, input().split())
seq = list(map(int, input().split()))

left, right = seq[:N//2], seq[N//2:]
leftSum, rightSum = [], []

getSum(left, leftSum)
getSum(right, rightSum)

answer = 0
for L in leftSum:
    target = S - L
    answer += getCount(rightSum, target)

answer += getCount(leftSum, S)
answer += getCount(rightSum, S)

print(answer)