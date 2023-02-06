# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline
arr = [int(input()) for _ in range(int(input()))]
stack = []
visited = [False] * (len(arr)+1)
answer = []
maxNum = 1
for num in arr:
    if stack and num == stack[-1]:
        maxNum = stack.pop()
        visited[num] = True
        answer.append("-")
    elif stack and num < stack[-1]:
        answer = "NO"
        break
    elif not stack:
        for i in range(maxNum,num+1):
            if not visited[i]:
                stack.append(i)
                answer.append("+")
                visited[i] = True
        maxNum = stack.pop()
        answer.append("-")

    else:
        for i in range(stack[-1],num+1):
            if not visited[i]:
                stack.append(i)
                answer.append("+")
                visited[i] = True
        maxNum = stack.pop()
        answer.append("-")

if answer == "NO":
    print(answer)
else:
    print(*answer, sep="\n")

# def sol(seq):
#     i = 1
#     ans = []
#     stack = []
#     for num in seq:
#         while i <= num:
#             stack.append(i)
#             ans.append('+')
#             i += 1

#         if stack.pop() != num: return "NO"
#         ans.append('-')
#     return '\n'.join(ans)