# https://school.programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    dist = [rocks[0]]
    dist += [rocks[i+1] - rocks[i]for i in range(len(rocks)-1)]
    dist.append(distance-rocks[-1])
    
    left = 0
    end = distance
    
    while left < end:
        mid = (left + end)//2
        stones = 0
        current = 0
        for d in dist:
            current += d
            if current < mid:
                stones += 1
            else:
                current = 0
        if stones <= n:
            left = mid + 1
        else: end = mid
        
    return left - 1