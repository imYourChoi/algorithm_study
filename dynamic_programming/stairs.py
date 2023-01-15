# https://www.acmicpc.net/problem/2579

# n = int(input())
# stairs = [0] + [int(input()) for _ in range(n)]

# def stair():
#     dp = [[0,0,0]]

#     while True:
#         temp = []
#         flag = True
#         for score, location, cont in dp:
#             if location == n:
#                 temp.append([score, location, cont])
#                 continue
#             if cont < 2 and location + 1 <= n:
#                 temp.append([score + stairs[location+1], location + 1, cont+1])
#                 flag = False
#             if location + 2 <= n:
#                 temp.append([score + stairs[location+2], location + 2, 1])
#                 flag = False
#         if flag:
#             break
#         dp = temp
#     answer = 0
#     for i in dp:
#         answer = max(answer, i[0])

#     return answer

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

def stair():
    if n == 1:
        return stairs[1]
    array = [[0,0], [stairs[1],0], [stairs[1]+stairs[2], stairs[2]]] + [[0,0] for _ in range(n-2)]
    for i in range(3,n+1):
        array[i][0] = array[i-1][1] + stairs[i]
        array[i][1] = max(array[i-2][0], array[i-2][1]) + stairs[i] if i-2 >= 0 else 0
    
    return max(array[-1])
    
print(stair())