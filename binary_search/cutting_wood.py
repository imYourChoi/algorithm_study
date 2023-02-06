# https://www.acmicpc.net/problem/2805

n,m=map(int, input().split())

trees = sorted(map(int, input().split()))

start = 0
end = trees[-1]
ans = 0

while start <= end:
    mid = (start+end)//2
    tree = sum([tree-mid for tree in trees if tree > mid])
    if tree >= m:
        ans = mid
        start = mid+1
    else:
        end = mid-1
    # if tree == m:
    #     ans = mid
    #     break
    # elif tree < m:
    #     end = mid-1
    # else:
    #     ans = mid
    #     start = mid+1

print(ans)