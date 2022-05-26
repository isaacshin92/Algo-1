import sys
from queue import Queue

sys.stdin = open('sample_input.txt')

def safeDir(dx, dy):
    rlt = False
    if 0 <= dx < N and 0 <= dy < N:
        rlt = True
    return rlt

def bfs(x,y):
    que.append((x,y))
    distance = [[0]*N for _ in range(N)]
    # print(f'distance: {distance}')
    while que:
        sx, sy = que.pop(0)
        if maze[sx][sy] == 0 or 2:
            maze[sx][sy] = 1

        #인접 인덱스 확인
        for _x, _y in dir:
            wx = sx + _x
            wy = sy + _y

            if safeDir(wx,wy): # board를 벗어나는지체크
                if maze[wx][wy] == 0: # 길이면 
                    # 그 길 인덱스와 동일한 위치에 시작점으로부터 거리를 표시 
                    distance[wx][wy] += distance[sx][sy] + 1 
                    #큐에 다음으로 진행 할 좌표를 추가. 
                    que.append((wx,wy))
                elif maze[wx][wy] == 3:
                    return distance[sx][sy]
    # while문이 종료된 시점 == 3까지 도달하지 못한 것.
    return 0





T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dir =[(-1,0),(1,0),(0,1),(0,-1)]
    que = []
    maze = list()

    for i in range(N):
        maze.append(list(map(int,input())))

    # print(f'maze : {maze}')
    #2. 출발좌표 찾기 
    
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
                break
    
    print(f'#{test_case} {bfs(x,y)}')