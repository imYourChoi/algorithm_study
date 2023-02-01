# https://www.acmicpc.net/problem/15654

n,m=map(int, input().split())
nums=sorted(list(map(int, input().split())))

def dfs(arr, seq, index):
    if index == 1:
        for num in arr:
            print(*seq, num)
    else:
        for num in arr:
            new = arr[:]
            new.remove(num)
            dfs(new, seq + [num], index-1)

dfs(nums, [], m)