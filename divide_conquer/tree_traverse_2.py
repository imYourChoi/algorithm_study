# https://www.acmicpc.net/problem/2263

import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
answer = []

position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i

def traverse(inStart, postStart, length):
    root = postorder[postStart+length-1]
    rootIdx = position[root]
    print(root, end=" ")

    if rootIdx > inStart:
        traverse(inStart, postStart, rootIdx-inStart)
    if rootIdx < inStart+length-1:
        traverse(rootIdx+1, postStart+(rootIdx-inStart), length-(rootIdx-inStart)-1)

traverse(0, 0, len(inorder))
print()
