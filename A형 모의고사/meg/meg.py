import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def bfs(R,C):
    visited[R][C] = 1
    stack = [[R, C]]    
    cnt = 1
    while stack:
        
        a, b = stack.pop(0)
        pipe = ground[a][b] # pip type check
        
        for y, x in tunnel[pipe]: # connection check
            wy = a + y
            wx = b + x
            if  0 <= wy < N and 0 <= wx < M:# ground 범위 벗어나는지 체크 
                if (-y, -x) in tunnel[ground[wy][wx]]: # 연결 가능한지 확인. 
                    if not visited[wy][wx]: # 이전에 방문 X 
                        visited[wy][wx] = visited[a][b] + 1 # 이동 횟수 제약 조건 확인하기 위해, 이전 위치 값 += 1 으로 이동거리 체크 
                        stack.append([wy, wx]) # 다음 방문 하기 위해 stack 에 저장. 
                        if visited[wy][wx] <= L: # 방문한 위치에 숫자가 이동거리를 넘지 않을 때까지 
                            cnt += 1
    return cnt 
for tc in range(1, T + 1):
    # 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
    N, M, R, C , L = map(int,input().split())
    visited = [[0] * M for _ in range(N)]
    tunnel = {
    0: [()],
    1: [(-1, 0),(1, 0), (0, 1), (0, -1)], # 상하좌우
    2: [(1, 0), (-1, 0)],  # 상 하 
    3: [(0, 1), (0, -1)], # 좌 우 
    4: [(-1, 0), (0, 1)], # 상 우 
    5: [(1, 0), (0, 1)], # 하 우 
    6: [(1, 0), (0, -1)], # 하 좌 
    7: [(-1, 0), (0, -1)] # 상 좌 
}
    ground = []
    for i in range(N):
        ground.append(list(map(int,input().split())))
    
    result = bfs(R,C)

    # print(f's_pipe: {s_pipe}')
    
    # BFS(R, C, s_pipe)

    print(f'#{tc} {result}')

    
    # for i in range(len(ground)):
    #     print(f'{ground[i]} \n')
    # print('\n')