import sys
sys.stdin = open('sample_input.txt')

def childCnt(root):
    child_stack = []
    child_stack.append(root)
    cnt = 0
    #subtree node 갯수 찾기 
    while child_stack:
        r = child_stack.pop()
        for j in board[r]:
            if j != 0:
                cnt += 1
                child_stack.append(j)
    return cnt

T = int(input())

    # 이진 트리임으로 => 각 노드는 최대 두개씩의 자식을 가진다. 
    #간선의 갯수가 주어짐으로, 가능한 최대 깊이만큼 이중리스트를 선언
for test_case in range(1, T + 1):
    rlt = 0
    edge_cnt, sub_tree_root = map(int,input().split())
    board = [[0]*(edge_cnt + 2) for _ in range(edge_cnt + 2)]
    edge_rel = list(map(int,input().split()))

    for i in range(0,len(edge_rel) -1,+2):
        idx = edge_rel[i]
        child = edge_rel[i+1]
        board[idx][child] = child

    rlt = childCnt(sub_tree_root)
    result = rlt + 1
    print(f'#{test_case} {result}')





