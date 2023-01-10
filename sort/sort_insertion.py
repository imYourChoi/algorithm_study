array = [int(input()) for _ in range(int(input()))]

for i in range(1, len(array)):
    temp = i
    while array[temp] < array[temp-1] and temp > 0:
        array[temp], array[temp-1] = array[temp-1], array[temp]
        temp -= 1

for x in array:
    print(x)