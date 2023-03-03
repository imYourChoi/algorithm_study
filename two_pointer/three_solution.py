# https://www.acmicpc.net/problem/2473

n = int(input())
solutions = sorted(list(map(int, input().split())))

def sol():
    answer = (None, None, None)
    smallest = float('inf')
    for i in range(n-2):
        selected = solutions[i]
        start = i+1
        end = n-1

        while start < end:
            current = selected + solutions[start] + solutions[end]

            if abs(current) < abs(smallest):
                smallest = current
                answer = (selected, solutions[start], solutions[end])

            if current < 0:
                start += 1
            elif current > 0: 
                end -= 1
            else:
                return answer
    return answer

print(*sol())