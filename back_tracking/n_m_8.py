# https://www.acmicpc.net/problem/15657

N,M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(array, track, index):
    if index == 1:
        for item in array:
            if not track or (track and track[-1] <= item):
                print(*track, item)
    else:
        for item in array:
            if not track or (track and item >= track[-1]):
                dfs(array, track + [item], index-1)

dfs(nums, [], M)