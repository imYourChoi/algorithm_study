# https://www.acmicpc.net/problem/17387

x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

def ccw(px1,py1,px2,py2,px3,py3):
    S = px1*py2 + px2*py3 + px3*py1 - (py1*px2 + py2*px3 + py3*px1)
    if S>0: return 1
    elif not S: return 0
    else: return -1

first = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)
second = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)

if not first and not second:
    if x1 > x2: x1,x2 = x2,x1
    if x3 > x4: x3,x4 = x4,x3
    if y1 > y2: y1,y2 = y2,y1
    if y3 > y4: y3,y4 = y4,y3
    print(1 if x3<=x2 and x1<=x4 and y3<=y2 and y1<=y4 else 0)
else:
    print(1 if first<=0 and second<=0 else 0)