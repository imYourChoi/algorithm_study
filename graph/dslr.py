# # https://www.acmicpc.net/problem/9019

from collections import deque
import sys, math
input = sys.stdin.readline

answer = []

def bfs():
    a,b = map(int, input().split())
    visited = [False] * 10000
    visited[a] = True

    queue = deque([(a,"")])

    while queue:
        for _ in range(len(queue)):
            current, command = queue.popleft()
            D = (current * 2) % 10000
            S = current - 1 if current else 9999
            L = (current % 1000) * 10 + current // 1000
            R = (current % 10) * 1000 + current // 10
            for num, op in zip([D,S,L,R], ["D", "S", "L", "R"]):
                if num == b:
                    answer.append(command+op)
                    return
                if not visited[num]:
                    queue.append((num, command + op))
                    visited[num] = True

for _ in range(int(input())): bfs()

print(*answer, sep="\n")

# 백준 풀이 참고

# import sys
# from collections import deque
# input = sys.stdin.readline

# commands = ['D', 'S', 'L', 'R', 'D']

# for _ in range(int(input())):
#     answer = ''
#     dp = [-1] * 10000
#     dpR = [-1] * 10000
#     a, b = map(int, input().rstrip().split(' '))
#     dp[a] = ''
#     dpR[b] = ''
#     queue = deque([(a, 'start'), (b, 'end')])
#     while queue:
#         current, type = queue.popleft()
#         if type == 'start':
#             D = (current * 2) % 10000
#             S = current - 1 if current else 9999
#             L = (current % 1000) * 10 + current // 1000
#             R = (current % 10) * 1000 + current // 10
#             for num, op in zip([D,S,L,R], commands):
#                 if dpR[num] != -1:
#                     answer = dp[current] + op + dpR[num]
#                     break
#                 if dp[num] == -1 or len(dp[num]) > (len(dp[current]) + 1):
#                     dp[num] = dp[current] + op
#                     queue.append((num, 'start'))
#         if type == 'end':
#             D = current // 2
#             S = 0 if current == 9999 else current + 1
#             L = (current % 10) * 1000 + current // 10
#             R = (current % 1000) * 10 + current // 1000
#             D2 = (current + 10000) // 2
#             for num, op in zip([D,S,L,R,D2], commands):
#                 if op in ["D", "D2"] and current % 2:
#                     continue
#                 if dp[num] != -1:
#                     answer = dp[num] + op + dpR[current]
#                     break

#                 if dpR[num] == -1 or len(dpR[num]) > (len(dpR[current]) + 1):
#                     dpR[num] = op + dpR[current]
#                     queue.append((num, 'end'))
#         if answer:
#             break

#     print(answer)