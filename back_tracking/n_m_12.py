# https://www.acmicpc.net/problem/15666

N,M = map(int,input().split())
arr = sorted(list(map(int, input().split())))

def dfs(arr, cur, index):
    temp = set()
    if index == 1:
        for num in arr:
            if num in temp:
                continue
            temp.add(num)
            if not cur or (cur and cur[-1] <= num):
                print(*cur, num)
    else:
        for num in arr:
            if num in temp:
                continue
            temp.add(num)
            if not cur or (cur and cur[-1] <= num):
                dfs(arr, cur + [num], index-1)

dfs(arr, [], M)