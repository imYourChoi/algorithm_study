N, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]
m, K = list(map(int, input().split()))
B = [list(map(int, input().split())) for i in range(m)]
answer = [[0 for _ in range(K)] for _ in range(N)]

for row in range(N):
    for column in range(m):
        for bColumn in range(K):
            answer[row][bColumn] += A[row][column] * B[column][bColumn]

for row in answer:
    print(" ".join(list(map(str, row))))