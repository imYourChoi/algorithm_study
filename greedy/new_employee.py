# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    employees = [list(map(int, input().split())) for _ in range(n)]
    employees.sort()
    temp = employees[0][1]
    answer = 1
    for employee in employees[1:]:
        if employee[1] < temp:
            answer += 1
            temp = employee[1]
    print(answer)