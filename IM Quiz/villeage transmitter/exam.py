import math,sys

sys.stdin = open('sample_input.txt')

test_case = int(input())

for tc in range(test_case):
    N = int(input()) + 1
    matrix = []
    home = []
    point = None

    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

        for j in range(N):
            if row[j] == 1:
                home.append([i, j])
            elif row[j] == 2:
                point = [i, j]

    max_distance = 0
    for coord in home:
        distance = (point[0] - coord[0]) ** 2 + (point[1] - coord[1]) ** 2
        max_distance = max(max_distance, distance)
    print(f"#{tc+1} {math.ceil(max_distance ** (1 / 2))}")
