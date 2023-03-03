# https://www.acmicpc.net/problem/2869

import math

a,b,v=map(int,input().split())
print(max(1 if v-a else 0,math.ceil((v-a)/(a-b)))+1)