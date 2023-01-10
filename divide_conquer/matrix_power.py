# https://www.acmicpc.net/problem/10830

N, B = list(map(int, input().split()))
answer = [list(map(int, input().split())) for _ in range(N)]

def multiply(m1, m2):
    result = []
    for row in range(len(m1)):
        temp = []
        for column in range(len(m2[0])):
            num = 0
            for m2Row in range(len(m2)):
                num += m1[row][m2Row] * m2[m2Row][column]
            temp.append(num % 1000)
        result.append(temp)

    return result
        

def power(matrix, index):
    if index == 1:
        return matrix

    mid = index // 2

    double = multiply(matrix, matrix)
    result = power(double, mid)

    if index % 2 == 1:
        result = multiply(result, matrix)

    return result

answer = power(answer, B)

for row in range(N):
    for column in range(N):
        answer[row][column] %= 1000

for row in answer:
    print(" ".join(list(map(str, row))))