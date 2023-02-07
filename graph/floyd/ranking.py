# https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import deque

def solution(n, results):
    answer = 0
    
    graph = [{} for i in range(n+1)]
    
    for a,b in results:
        graph[a][b] = 1
        graph[b][a] = -1
    
    for via in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if start == end or graph[start].get(end, 0) in [1,-1]:
                    continue
                if graph[start].get(via, 0) == graph[via].get(end, 0) == 1:
                    graph[start][end] = 1
                    graph[end][start] = graph[via][start] = graph[end][via] = -1
    for person in graph:
        if len(person) == n-1:
            answer += 1
        
    return answer