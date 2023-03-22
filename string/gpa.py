grade = 0
count = 0
level = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
for _ in range(20):
    i = input().split()
    if i[-1] == "P":
        continue
    count += float(i[-2])
    grade += level[i[-1]] * float(i[-2])

print(grade/count)