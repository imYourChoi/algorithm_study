# https://www.acmicpc.net/problem/15663

N,M = map(int,input().split())
arr = sorted(list(map(int, input().split())))

def dfs(arr, cur, index):
    temp = set()
    if index == 1:
        for num in arr:
            if num in temp:
                continue
            temp.add(num)
            print(*cur, num)
    else:
        for num in arr:
            if num in temp:
                continue
            temp.add(num)
            new = arr.copy()
            new.remove(num)
            dfs(new, cur + [num], index-1)

dfs(arr, [], M)