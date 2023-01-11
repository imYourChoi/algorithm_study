# https://www.acmicpc.net/problem/2609

a,b=sorted(map(int,(input().split())), reverse=True)

def gcd(a,b):
    Q = a // b
    R = a % b
    if R == 0:
        return b
    else: return gcd(b, R)

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))