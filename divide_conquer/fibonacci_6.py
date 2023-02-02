# https://www.acmicpc.net/problem/11444

n = int(input())
divide = 1000000007

def multiply(first, second):
    return [
        [(first[0][0]*second[0][0] + first[0][1]*second[1][0]) % divide,
        (first[0][0]*second[0][1] + first[0][1]*second[1][1]) % divide],
        [(first[1][0]*second[0][0] + first[1][1]*second[1][0]) % divide,
        (first[1][0]*second[0][1] + first[1][1]*second[1][1]) % divide],
    ]

def fibonacci(n):
    if n == 0:
        return [[0,0]]
    if n == 1:
        return [[1,1],[1,0]]

    matrix = fibonacci(n//2)
    multiple = multiply(matrix,matrix)

    if n % 2:
        return multiply(multiple, [[1,1],[1,0]])
    return multiple

print(fibonacci(n)[0][1])