https://www.acmicpc.net/problem/1259

def palindrome(n, l, r):
    if l >= r:
        return "yes"
    if n[l] == n[r]:
        return palindrome(n, l+1, r-1)
    return "no"

while True:
    n = input()
    if n == '0':
        break
    print(palindrome(n, 0, len(n)-1))
