# https://www.acmicpc.net/problem/1992

n = int(input())
array = [[int(x) for x in input().strip()] for x in range(n)]

def quad(array, row, column, index):
    if index == 1:
        return str(array[row][column])
    
    blackOrWhite = array[row][column]
    flag = True
    for r in range(row, row+index):
        for c in range(column, column+index):
            if array[r][c] != blackOrWhite:
                flag = False
    # print(whiteOrBlue)
    if flag == True:
        return str(blackOrWhite)
    if flag == False:
        string = "("
        for r in range(row, row+index, index//2):
            for c in range(column, column+index, index//2):
                string += quad(array, r, c, index//2)
        return string + ")"

string = quad(array, 0, 0, n)
print(string)