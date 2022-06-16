import sys 

sys.stdin = open('input.txt')

T = int(input())

def promising(v):
    for i in range(v):
        if row[v] == row[i] or abs(row[v] - row[i]) == v - i:
            return False
    return True

def dfs(v):
    global cnt
    
    if v == len(row) : 
        cnt += 1 
        
    else :
        for i in range(len(row)):
            row[v] = i 
            # print(f'row : {row}')
            if promising(v):
                dfs(v + 1)

for tc in range(1,T + 1):
    N = int(input())
    cnt = 0          # Queen을 배치할 수 있는 가짓수 체크
    row = [0] * N    # N 크기만큼의 row -> 여기에 놓은 것을 기준으로 판단할 것
    dfs(0)
    print(f'#{tc} {cnt}')