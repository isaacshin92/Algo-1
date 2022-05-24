# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
# 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

import sys 

sys.stdin = open('sample_input.txt')

def dfs(start, end):
    stack = [] 
    visited = [False] * (node_cnt + 1)  #방문 여부 기록 리스트
    stack.append(start) # 시작점을 stack 에 추가 
    
    while stack:
        v = stack.pop()
        visited[v] = True # stack 에서 pop 한 노드 방문 기록
        for w in range(node_cnt+1): # vertex 만큼 반복 
            if not visited[w]: # 방문 이력이 False 일때 
                if nodes[v][w]: # nodes 의 해당 index 값이 1인지 0인지 1 = true, 0 = false
                    stack.append(w)
    return visited[end]

T = int(input())

for test_case in range(1, T + 1):
    
    node_cnt, edge_cnt = map(int, input().split()) # V 개의 노드를 이어주는 E개의 간선
    nodes = [[0] * (node_cnt + 1) for _ in range(node_cnt + 1)]
    
    for _ in range(edge_cnt):
        x, y = map(int, input().split()) # 간선연결  정보 
        nodes[x][y] = 1
        
        
    result = 1
    start,  end = map(int,input().split()) # start, end
    
    if not dfs(start, end):
        result = 0
    
    print(f'#{test_case} {result}')
    
    
