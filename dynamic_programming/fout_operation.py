# https://school.programmers.co.kr/learn/courses/30/lessons/1843

def solution(arr):
    arr = [int(x) if x.isnumeric() else x for x in arr]
    inf = float('inf')
    n = len(arr) // 2 + 1
    answer = -1
    max_dp = [[-inf] * (n+1) for _ in range(n+1)]
    min_dp = [[inf] * (n+1) for _ in range(n+1)]
    
    for step in range(0,n+1):
        for i in range(1,n-step+1):
            j = i + step
            if step == 0:
                max_dp[i][i] = arr[(i-1)*2]
                min_dp[i][i] = arr[(i-1)*2]
            else:
                for k in range(i,j):
                    if arr[k*2-1] == "+":
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                    else:
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
    
    return max_dp[1][-1]