# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


# def compare(target):
#     to_list = list(target)
#     to_list.reverse()

#     if target == ''.join(to_list):
#         return True
#     else:
#         return False


# def slicing(target, len_str):
#     temp = ''
#     joined = ''.join(target)

#     for i in range(0, len(target) - len_str + 1):
#         temp = joined[i: len_str+i]

#         if compare(temp):
#             return temp

#     return False
    


# for test_case in range(1, T + 1):
#     result = ''

#     N, M = map(int, input().split()) # N = 글자판의 크기 NxN , M = 회문의 글자 수 .
#     board = list()
#     for i in range(N): # 2차원배열
#         board.append(list(input())) 

#     # print(f'board: {board}')



#     #slicing을 통해 회문의 글자수대로 자르면서 검사 !! 회문은 1개만 존재, 찾는 순간 break
#     for i in range(0, N-1):
#         result = slicing(board[i],M)
#         if result != False:
#             print(f'#{test_case} {result}')
#             break
#     if result == False: # 가로 탐색에서 결과를 찾지 못했을 경우 세로로 재검색.
#         #빈 중첩배열 선언
#         verticle = []
#         for i in range(10):
#             inner = []
#             verticle.append(inner)
#             for j in range(10):
#                 inner.append('')                

#         # 리스트의 세로에서 회문을 찾을 수 있도록 배열을 세로로 돌린다.
#         for i in range(10):
#             for j in range(10):
#                 verticle[j][i] = board[i][j]
#         # print(f'verticle: {verticle}')

#         #slicing을 통해 회문의 글자수대로 자르면서 검사 2
#         for i in range(0, N-1):
#             result = slicing(verticle[i],M)
#             if result != False:
#                 print(f'#{test_case} {result}')
#                 break
# import sys
# sys.stdin = open('sample_input.txt')

# def compare(line, len_str):
    
#     temp = '' #slicing temp 
#     result = ''

#     for i in range(0, len(line) - len_str +  1):
    
#         temp = line[i:len_str + i]
#         temp_list = list(temp)
#         temp_list.reverse()
#         rev = ''.join(temp_list)

#         if len(temp) == len_str:

#             if temp == rev:
#                 result = temp
#     return result


# T = int(input())
    
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split()) # N = 글자판의 크기 NxN , M = 회문의 글자 수 .
#     result = ''
#     board = list()
#     verticle = []

#     for i in range(N):
#         board.append(list(input()))

#     for i in range(0, N-1):
#         temp = ''.join(board[i])
#         rlt = compare(temp,M)

#         if len(rlt) > 0 :
#             result = rlt 
#             print(f'#{test_case} {result}')
#     if result == '':
#         #빈 중첩배열 선언
#         for i in range(10):
#             inner = []
#             verticle.append(inner)
#             for j in range(10):
#                 inner.append('')                

#         # 리스트의 세로에서 회문을 찾을 수 있도록 배열을 세로로 돌린다.
#         for i in range(10):
#             for j in range(10):
#                 verticle[j][i] = board[i][j]

#         for i in range(0, N-1):
#             temp = ''.join(verticle[i])
#             rlt = compare(temp,M)

#             if len(rlt) > 0:
#                 print(f'#{test_case} {rlt}')


import sys
sys.stdin = open('sample_input.txt')

def reverseCompare(board,target_size):
    temp = ''
    result = ''
    for i in range(len(board) - target_size + 1):
        temp = board[i: target_size + i + 1]
        # print(f'temp: {temp}')
        list_temp = list(temp)
        list_temp.reverse()
        revs = ''.join(list_temp)

        # if len(temp) >= target_size:
        if temp == revs:
            result = temp
    return result
        


T = int(input())

for test_case in range(1, T + 1):
    
    size, target = map(int, input().split())

    board = []
    verticle = []
    rlt = ''

    for i in range(size):
        board.append(input())

    for i in range(size):
        result = reverseCompare(board[i],target)

        if len(result) > 0:
            rlt = result


    for j in range(size):
        verticle.append([0]*size)

    for i in range(0, size):
        for j in range(size):
            verticle[i][j] = board[j][i]
        verticle[i] = ''.join(verticle[i])
    

    for i in range(0, size):
        result = reverseCompare(verticle[i],target)
        if len(result) > 0:
            rlt = result
    print(f"#{test_case} {rlt}")