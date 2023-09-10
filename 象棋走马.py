

ListDistance = input().rstrip('\n').split(',')
m, n, x, y = int(ListDistance[0]), int(ListDistance[1]), int(ListDistance[2]), int(ListDistance[3])
def searchwidth(x, y, m, n):
    count=0
    PointNow.append((x,y,count))
    ListPoint[x][y]=1
    while PointNow:
        tuplePoint=PointNow.pop(0)
        x1,y1,count=tuplePoint[0],tuplePoint[1],tuplePoint[2]
        for i in range(8):
            nextx1=x1+WayTuple[i][0]
            nexty1=y1+WayTuple[i][1]
            if nextx1 == m and nexty1 == n:
                return count+1
            elif m >= nextx1 >= 0  and 0 <= nexty1 <= n:
                if ListPoint[nextx1][nexty1]==0:
                    PointNow.append((nextx1,nexty1,count+1))
                    ListPoint[nextx1][nexty1]=1


ListPoint = [[0 for i in range(n+1)] for j in range(m+1)]
WayTuple = ((1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1))
PointNow = []
if searchwidth(x, y, m, n) is None:
    print(-1)
else:
    print(searchwidth(0,0,m,n))
