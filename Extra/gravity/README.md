### 중력과 2차원 배열의 회전은 불필요하다. 
> 결국, 가장 높이 쌓여있는 박스의 인덱스를 최대 낙차값에서 뺀 값이 결과값이다. 

```python

import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    width, height = map(int, input().split())
    result = 0
    board = [[0]* width for _ in range(height)]

    boxes = list(map(int, input().split()))

    print(f'length of boxes : {len(boxes)}')
    
    # 낙차가 된 박스의 상황을 가정
    for i in range(len(boxes)):
        # i의 최대 낙차 값은 len(data) - (i+1)
        # i 이후의 모든 행을 검사
        max_height = len(boxes) - (i+1)
        print(f'max_height: {max_height}')
        # i의 다음 행부터 박스 끝까지 반복 
        for j in range(i+1, len(boxes)):
            # 위에 있는 행(i)보다
            # 아래 있는 행(j)이 상자가 더 많은 경우
            if boxes[i] <= boxes[j]:
                # 최대 낙차 값은 1 감소
                max_height -= 1

        # 낙차의 최댓값 도출
        if result < max_height:
            result = max_height

    print('#{} {}'.format(test_case, result))

```