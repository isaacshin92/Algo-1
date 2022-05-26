import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = list()
    for i in range(N):
        board.append(list(map(int, input().split(' '))))
    # print(f'board = {board}')

    # stack = [] # 고른 최소값 쌓기. 
    positions = [] # 고른 값의 x index 값
    rlt = 0
    # 시작점
    min = 10
    for i in range(N):
        for j in range(N):
            if board[i][j] < min and j not in positions:
                    if len(positions) == i:
                        positions.append(j)
                    elif len(positions) == i + 1:
                        positions.pop()
                        positions.append(j)
                    min = board[i][j]
        # print(f'[{i}]positions: {positions}')
        rlt += min
        # print(f'min: {min}')
        min = 10        

    print(f'#{test_case} {rlt}')