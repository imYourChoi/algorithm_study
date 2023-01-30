# https://www.acmicpc.net/problem/14889

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = float('inf')

def dfs(array, seq, index):
    if index == n/2:
        global answer
        new = list(set([x for x in range(n)]) - set(seq))
        first = sum([arr[seq[i]][seq[j]]+arr[seq[j]][seq[i]] for i in range(n//2) for j in range(i+1,n//2)])
        second = sum([arr[new[i]][new[j]]+arr[new[j]][new[i]] for i in range(n//2) for j in range(i+1,n//2)])
        answer = min(answer, abs(first-second))
    else:
        for x in array:
            if not seq or (seq and x > seq[-1]):
                new = array[:]
                new.remove(x)
                dfs(new, seq + [x], index + 1)

dfs([x for x in range(1,n)], [0], 1)

print(answer)

# n = int(input())
# board = [list(map(int,input().split())) for _ in range(n)]
# visited = [False for _ in range(n)]
# answer = float('inf')

# def dfs(index):
#     global answer
#     if index == n//2:
#         A,B = 0,0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i] and visited[j]:
#                     A += board[i][j]
#                 elif not visited[i] and not visited[j]:
#                     B +=board[i][j]
#         answer = min(answer, abs(A-B))
#         return
#     for i in range(index,n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(index+1)
#             visited[i] = False
            
# dfs(0)
# print(answer)