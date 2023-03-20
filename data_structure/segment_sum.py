# https://www.acmicpc.net/problem/2042

import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
array = [int(input()) for _ in range(N)]
answer = []
tree = [0 for _ in range(3000000)]

def make_tree(node, start, end):
    if start == end:
        tree[node] = array[start]
    else:
        mid = (start + end)//2
        tree[node] = make_tree(node*2, start, mid) + make_tree(node*2+1, mid+1, end)
    return tree[node]

def get_sum(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end)//2
    return get_sum(node*2, start, mid, left, right) + get_sum(node*2+1, mid+1, end, left, right)

def update_sum(node, start, end, pos, diff):
    if not start <= pos <= end:
        return
    
    tree[node] += diff
    if start == end:
        return
    mid = (start+end)//2
    update_sum(node*2,start,mid,pos,diff)
    update_sum(node*2+1,mid+1,end,pos,diff)

make_tree(1,0,N-1)

for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        diff = c - array[b-1]
        array[b-1] = c
        update_sum(1,0,N-1,b-1,diff)
    if a == 2:
        answer.append(get_sum(1,0,N-1,b-1,c-1))

print(*answer,sep="\n")