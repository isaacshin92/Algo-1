import sys
# 돌의 색이 1이면 흑돌, 2이면 백돌이다.

sys.stdin = open('sample_input.txt')

def safeDir(y,x):
    result = True
    if x < 0 or y < 0 or x > N or y > N :
        result = False
    return result

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,input().split()) # N = 보드의 크기 N x N , M = 돌을 놓는 횟수 
    board = [[0]*(N + 1) for _ in range(N + 1)] # 인덱스 값을 위해 벽 만들기. 

    board[(N//2)][(N//2)] = 2
    board[(N//2)][(N//2 + 1)] = 1
    board[(N//2) + 1][(N//2)] = 1
    board[(N//2) + 1][(N//2 + 1)] = 2
    
    dir =[(1,0),(-1,0),(0,1),(0,-1), (-1,-1),(-1,1),(1,1),(1,-1)]  # y,x directions
        
    for turn in range(M):
        x, y, c = map(int,input().split())
        
        #1. 돌 놓고
        print(f'x: {x}, y: {y} c : {c}')
        board[y][x] = c 
        # for i in range(len(board)):
        #     print(f'{board[i]} \n')  
        
        # 2. 주변 살핀다.  
        for x_,y_ in dir:

            x_check = x + x_
            y_check = y + y_  
            
            # x_check_nxt = x + x_ + x_
            # y_check_nxt = y + y_ + y_  

            if safeDir(y_check, x_check):
                    if c == 2: 
                        for j in range((N//2)):
                            if board[x_check][y_check] == 1:
                                if  0 < x_check + x_  <= N and 0 < y_check + y_ <= N:
                                    if board[x_check +x_][y_check + y_] != 0:
                                        board[x_check][y_check] = 2
                                        x_check += x_
                                        y_check += y_
                            elif board[x_check][y_check] == 2:
                                break
                    else:
                        for j in range(((N//2))):
                            if board[x_check][y_check] == 2 :
                                if  0 < x_check + x_  <= N and 0 < y_check + y_ <= N:
                                    if board[x_check +x_][y_check + y_] != 0:
                                        
                                        board[x_check][y_check] = 1
                                        x_check += x_
                                        y_check += y_
                            elif board[x_check][y_check] == 1:
                                break
                        
        print('--------------------------------')
        for i in range(len(board)):
            print(f'{board[i]} \n')
        print('\n')
        print('--------------------------------')
        
    b_cnt = 0
    w_cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1 

    print(f'{test_case} {b_cnt} {w_cnt}')
