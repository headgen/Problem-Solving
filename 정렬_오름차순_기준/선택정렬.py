def selection(array):
    for i in range(len(array)):
        # 정렬되지 않은 리스트에서 맨 앞 원소의 인덱스 i를 기준점으로 삼음
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

print(selection([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))