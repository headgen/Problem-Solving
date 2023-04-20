def insertion(array):
     # 첫 번째 값(index=0)은 정렬되었다고 가정하고 index를 1부터 진행
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:  # 한 칸씩 왼쪽으로 이동
                 array[j], array[j-1] = array[j-1], array[j]
            else:
                break
               
    return array

print(insertion([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))