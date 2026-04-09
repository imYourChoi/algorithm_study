# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    # 1. 행렬 초기화
    matrix = [[(i * columns) + (j + 1) for j in range(columns)]
              for i in range(rows)]
    result = []

    for x1, y1, x2, y2 in queries:
        # 0-indexed로 변경
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

        # 시작점의 값을 보관 (이 자리가 빈 칸이 됨)
        tmp = matrix[x1][y1]
        min_val = tmp

        # 2. 왼쪽 변: 아래에서 위로 올리기
        for k in range(x1, x2):
            matrix[k][y1] = matrix[k+1][y1]
            min_val = min(min_val, matrix[k][y1])

        # 3. 아래쪽 변: 오른쪽에서 왼쪽으로 당기기
        for k in range(y1, y2):
            matrix[x2][k] = matrix[x2][k+1]
            min_val = min(min_val, matrix[x2][k])

        # 4. 오른쪽 변: 위에서 아래로 내리기
        for k in range(x2, x1, -1):
            matrix[k][y2] = matrix[k-1][y2]
            min_val = min(min_val, matrix[k][y2])

        # 5. 위쪽 변: 왼쪽에서 오른쪽으로 당기기
        for k in range(y2, y1, -1):
            matrix[x1][k] = matrix[x1][k-1]
            min_val = min(min_val, matrix[x1][k])

        # 6. 보관했던 tmp를 마지막 빈자리에 넣기
        matrix[x1][y1+1] = tmp
        result.append(min_val)

    return result
