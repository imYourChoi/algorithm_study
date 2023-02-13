# https://www.acmicpc.net/problem/1439

s = input()
if "0" not in s or "1" not in s:
    print(0)
else:    
    s = s.replace("10", "1.0")
    s = s.replace("01", "0.1")
    arr = s.split(".")
    d = {"0": 0, "1": 0}
    for piece in arr:
        d[piece[0]] += 1
    print(min(d["0"], d["1"]))