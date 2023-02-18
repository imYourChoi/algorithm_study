# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**8)

bst = []
while True:
    try: bst.append(int(input()))
    except: break

n = len(bst)
def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for idx in range(start+1, end+1):
        if bst[start] < bst[idx]:
            mid = idx
            break
    
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(bst[start])

postorder(0, n-1)