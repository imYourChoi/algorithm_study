# https://www.acmicpc.net/problem/10844

n = int(input())

ds = [{1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}, {0:1, 1:1, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:1}]
for i in range(2, n):
    temp = {}
    for key in range(0, 10):
        if key == 0:
            temp[1] = ds[-1][0]
        elif key == 9:
            temp[8] += ds[-1][9]
        else:
            if key + 1 in temp:
                temp[key+1] += ds[-1][key]
            else:
                temp[key+1] = ds[-1][key]
            if key - 1 in temp:
                temp[key-1] += ds[-1][key]
            else:
                temp[key-1] = ds[-1][key]
    ds.append(temp)

print(sum(ds[n-1].values()) % 1000000000)