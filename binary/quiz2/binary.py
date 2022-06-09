import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    #각 보드는 5줄
    board = [['?'] * 15 for _ in range(5)]
    result =''
    for i in range(5):
        str = list(input())
        for j in range(len(str)):
            board[i][j] = str[j]

    # print(f'board: {board}')
    # for i in range(5):
    #     print(board[i])
    #     print('\n')
        
    for i in range(15):
        for j in range(5):
            if board[j][i] != '?':
                result += board[j][i]
    print(f'#{tc} {result}')
    
    