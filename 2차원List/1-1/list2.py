# 10x10 격자에 빨간색과 파란색을 칠한다. 
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어진다 
# 색이 겹치는 칸 갯수 출력

# test_case result : 
#1 4
#2 5
#3 7	

from os import rename
import sys
import pprint
from unittest import case

from pyparsing import col

sys.stdin = open('sample_input.txt')


T = int(input())


for test_case in range(1, T + 1):
    square_num = int(input()) # 칠할 네모 갯수 
    square_list = list()
    purple_count = 0 # number of purple squares
    # 10 X 10 2차원 배열 만들기 
    canvas = list()
    for i in range(10):
        innerArray = list()
        for j in range(10):
            innerArray.append(0)
        canvas.append(innerArray)
        
    #칠해야하는 네모 2차원 배열로 받기
    # for i in range(square_num):
    #     square_list.append(list(map(int,input().split())))
    
    # print(f'left_x : {left_x}, left_y : {left_y} \n right_x : {right_x},  right_y : {right_y} \n color : {color}')
    
    
    # 2차원 배열 돌면서 색 칠하기 칠하는 도중, 1,2 가 이미 값으로 존재할 경우 칠하고 puple_count += 1 <<- result
    for s in range(square_num):
        left_x, left_y, right_x, right_y, color = map(int,input().split())
        for i in range(left_x, right_x + 1):
            for j in range(left_y, right_y + 1):
                if color == 1:
                    if canvas[i][j] == 0:   
                        canvas[i][j] = 1
                    else:
                        canvas[i][j] = 3
                        purple_count += 1
                elif color == 2:
                    if canvas[i][j] == 0:
                        canvas[i][j] = 2                
                    else:
                        canvas[i][j] = 3
                        purple_count += 1

    for i in canvas:
        print(i)
    print(f'#{test_case} {purple_count}')
    

    
    
    
    # 이렇게 풀이했을 때, 3을 중복 카운트하는 버그가 발생하여 결과값이 상이하였다. 
    # 인덱스 값을 검사했을 때 이미 값이 3이라면 pass 를 하던지, 0,1,2에 대한 모든 경우를 if로 감싸줘야한다. 
    if canvas[i][j] == 0:
        canvas[i][j] = color
    else: 
        canvas[i][j] = 3
        purple_count += 1
        