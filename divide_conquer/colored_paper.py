# https://www.acmicpc.net/problem/2630

n = int(input())
array = [list(map(int, input().strip().split())) for x in range(n)]

def color(array, row, column, index):
    if index == 1:
        if array[row][column]:
            return 0, 1
        return 1, 0
    whiteOrBlue = array[row][column]
    flag = True
    for r in range(row, row+index):
        for c in range(column, column+index):
            if array[r][c] != whiteOrBlue:
                flag = False
    # print(whiteOrBlue)
    if flag == False:
        white, blue = 0, 0
        for r in range(row, row+index, index//2):
            for c in range(column, column+index, index//2):
                w, b = color(array, r, c, index//2)
                white += w
                blue += b
        return white, blue
    
    if whiteOrBlue == 0:
        return 1, 0
    elif whiteOrBlue == 1:
        return 0, 1

white, blue = color(array, 0, 0, n)
print(white)
print(blue)
# for x in array:
#     print(x)
# print(array)