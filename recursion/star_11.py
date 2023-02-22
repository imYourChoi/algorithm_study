# https://www.acmicpc.net/problem/2448

def star(n):
    width = n//3*5 + (n//3-1)
    height = n
    pattern = [[' ' for _ in range(width)] for _ in range(height)]

    def fill_triangle(x, y, size):
        if size == 3:
            pattern[y][x] = "*"
            pattern[y+1][x-1] = pattern[y+1][x+1] = "*"
            for i in range(x-2,x+3):
                pattern[y+2][i] = "*"
            return
        
        width = size//3*5 + (size//3-1)
        fill_triangle(x, y, size//2)
        fill_triangle(x - ((width-1)//4+1), y+size//2, size//2)
        fill_triangle(x + ((width-1)//4+1), y+size//2, size//2)

    fill_triangle(width//2, 0, n)
    for row in pattern:
        print(''.join(row))

star(int(input()))