import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())


    # 리프 노드 idx 자리에 값 넣기. 
    nodes_val = [0] * (N + 2)
    for i in range(M):
        idx, val = map(int, input().split())
        nodes_val[idx] = val

    #리프 연결관계 그리기 
    nodes_rel = [[0]*2 for _ in range(N + 2)]

    v = 0
    for i in range(1, N +1):
        nodes_rel[i][0],nodes_rel[i][1] = i+v+1, i+v+2
        v += 1

    for i in range(1, len(nodes_rel) -1):
        print(f'{i}노드는 {nodes_rel[i]} 와 연결되어있다. ')
    print('\n')

    

    

    