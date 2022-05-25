#  0은 통로, 1은 벽, 2는 출발, 3은 도착
import sys
sys.stdin = open('sample_input.txt')

def safeDir(x,y):
    rlt = True
    if x < 0 or y < 0 or x >= N or y >= N:
        rlt = False
    return rlt

def move(x,y):

    global result

    #????
    if maze[x][y] == 3 or result is False:
    # if maze[x][y] == 3 or result:
        result = 1
    else:
        for x_, y_ in dir:
            dx = x + x_ 
            dy = y + y_
            
            if safeDir(dx, dy):
                if maze[dx][dy] != 1:
                    maze[x][y] = 1
                    move(dx, dy)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 미로의 크기
    dir = [(0, -1),(0, 1), (-1, 0), (1, 0)]
    result = 0
    maze =[]

    # 미로에 벽 정보 받기.
    for i in range(N):
        maze.append(list(map(int,input())))

    #출발 지점 찾기 .
    x, y = 0, 0
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                x, y = i, j 
                move(x,y)        

    print(f'#{test_case} {result}')


    #maze print
    # for i in range(len(maze)):
    #     print(f'{maze[i]} \n')
    # print('\n')