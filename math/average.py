# https://www.acmicpc.net/problem/4344

for _ in range(int(input())):
    N, *score = map(int, input().split())
    average = sum(score) / len(score) 
    print("%.3f%%" % (len([x for x in score if x > average])/N*100))