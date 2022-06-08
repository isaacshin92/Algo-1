import sys

sys.stdin = open('sample_input.txt')

T = 10

def test(l1, l2, b, r1, r2):
    # 
    global view
    left_top = 0
    right_top = 0
    higher = 0 
    
    if b > l1 and b > l2 and b > r1 and b > r2: # 왼쪽, 오른쪽 모두 2칸 조경 확보 되었을 때, 
        left_top = max(l1, l2)
        right_top = max(r1, r2)
        if left_top == right_top:
            view += b - left_top
        else:
            higher = max(left_top, right_top)
            view += b - higher

for tc in range(1, T + 1):
    N = int(input())
    view = 0
    # 첫 번째 input() == 가로  ㅇ건물의 높이는 255 개가 최대 높이
    buildings = list(map(int, input().split()))
    
    for i in range(N):
        if buildings[i]  != 0: # if a building is there
            test(buildings[i -2],buildings[i -1], buildings[i], buildings[i + 1], buildings[i + 2])
    
    print(f'#{tc} {view}')
    