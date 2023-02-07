# https://www.acmicpc.net/problem/5525

n,m,s = int(input()), int(input()), input()

answer, idx, count = 0,0,0

while idx < m - 2:
    if s[idx:idx+3] == "IOI":
        idx += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        idx += 1
        count = 0

print(answer)

# sub = "I" + "OI" * n
# answer = 0
# for i in range(m-(n*2)):
#     if s[i:i+len(sub)] == sub:
#         answer += 1
# print(answer)