## Bubble sorting


arr = [4,25,77,32,125,136,3568,4,2,3,234,6,1445,34,74562,351]


# 한 바퀴 돌 때마다 비교해야하는 값이 하나씩 줄어듦 -> 가장 큰 값이 가장 오른쪽으로 쌓이기 때문에 하나씩 index 값을 줄여줘야 한다.
for i in range(len(arr)-1, 0, -1): # 배열크기 -1 부터 0까지 한번 돌 때마다 -1
    for j in range(len(arr) -1): # 두개씩 쌍을 지어 비교함으로, 마지막 인덱스까지 가면 out of bounds 에러가 나오기 때문에 -1 해준다. 
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1] , arr[j] # 비교 후 위치 변경 

print(f'arr : {arr}')


#카운팅 정렬 (계수 정렬)







