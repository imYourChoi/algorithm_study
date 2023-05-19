# https://www.acmicpc.net/problem/20040

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n,m = map(int, input().split())

parent = [x for x in range(n+1)]

def find_root(a):
    if a == parent[a]: return a
    parent[a] = find_root(parent[a])
    return parent[a]

def union_root(a,b):
    A = find_root(a)
    B = find_root(b)

    if A == B: return True
    parent[B] = A
    return False

answer = 0
for i in range(m):
    a,b = map(int, input().split())
    if union_root(a, b): 
        answer = i+1
        break

print(answer)