# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
# 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

import sys

sys.stdin = open('sample_input.txt')

def dfs(start, end):
    visited = [False] * (V + 1)
    stack =[]
    stack.append(start) 
    
    while stack:
        v = stack.pop()
        visited[v] = True
        
        for w in range(V + 1):
            if not visited[w]:
                if vertexs[v][w]:
                    stack.append(w)
    return visited[end]
    
    

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int,input().split())
    
    # vertexs = [[0] * range(E + 1) for _ in range(E + 1)]
    vertexs = list()
    
    for _ in range(V + 1):
        inner = []
        for _ in range(V + 1):
            inner.append(0)
        vertexs.append(inner)
    
    for _ in range(E):
        x, y = map(int,input().split())
        vertexs[x][y] = 1
        
    start, end = map(int,input().split())
    
    result = 1
    
    if not dfs(start, end):
        result = 0
    print(f'#{test_case} {result}')