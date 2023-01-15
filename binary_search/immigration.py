# https://school.programmers.co.kr/learn/courses/30/parts/12486

def solution(n, times):
    answer = 0
    start = 1
    end = times[-1] * n
    mid = 0
    
    while start < end:
        mid = (start + end) // 2
        s = 0
        for time in times:
            s += mid // time
        
        if s >= n:
            end = mid
        else:
            start = mid + 1
    
    answer = mid + 1
    return answer