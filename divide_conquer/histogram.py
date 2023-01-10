# https://www.acmicpc.net/problem/6549

array = []

while True:
    arr = input()
    if arr == '0':
        break
    array.append(list(map(int, arr.split())))

# def histogram(array):
#     if len(array) == 1:
#         return array[0]

#     value = len(array) * min(array)
#     left, right = histogram(array[:-1]), histogram(array[1:])

#     return max([value, left, right])

def histogram(array):
    answer = []
    maxHeight = 0

    for idx, val in enumerate(array):
        if len(answer) == 0:
            answer.append([idx, val])
            continue
        flag = False
        temp = None
        while len(answer) > 0 and answer[-1][1] > val:
            flag = True
            last = answer.pop()
            maxHeight = max(maxHeight, last[1] * (idx - last[0]))
            temp = [last[0], val]
        if flag:
            answer.append(temp)
        answer.append([idx, val])
    
    for item in answer:
        maxHeight = max(maxHeight, item[1] * (len(array) - item[0]))
    return maxHeight

for arr in array:
    print(histogram(arr[1:]))
