array = [int(input()) for _ in range(int(input()))]

for i in range(0, len(array) - 1):
    temp = i
    for j in range(i + 1, len(array)):
        if array[j] < array[temp]:
            temp = j
    array[i], array[temp] = array[temp], array[i]

for x in array:
    print(x)