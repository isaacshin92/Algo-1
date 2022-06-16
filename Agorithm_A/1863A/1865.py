import sys

sys.stdin = open('input.txt')


def search(w, per):
    global result

    # 가지치기
    if per <= result:
        return

    # 종료 조건
    if w == N:
        result = max(result, per)
        return

    # 아직 모든 일꾼이 선택되지 않았을 때
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1  # 첫번 째 업무 방문 처리  .
                search(w + 1, per * arr[w][i])  # dfs
                visited[i] = 0  # 이 다음 dfs할 준비


T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    visited = [0] * N
    result = 0

    search(0, 1)

    print(f'#{tc} {result*100:6f}')