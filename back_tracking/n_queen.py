# https://www.acmicpc.net/problem/9663

# n = int(input())

# answer = 0

# def chess(arr):
#     global answer
#     if len(arr) == n:
#         answer += 1
#         return
#     for i in range(n):
#         flag = True
#         for idx, val in enumerate(arr):
#             if val == i or abs(i - val) == len(arr)-idx:
#                 flag = False
#                 break
#         if flag:
#             chess(arr+[i])

n = int(input())
board = [0 for _ in range(n)]
answer = 0

def chess(arr, index):
    global answer
    if index == n:
        answer += 1
        return
    for x in range(n):
        flag = True
        for y in range(index):
            if board[y] == x or abs(x - board[y]) == index-y:
                flag = False
                break
        if flag:
            arr[index] = x
            chess(arr, index+1)

chess(board, 0)
print(answer)