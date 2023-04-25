# Hoare partition
def partition(array, pivot_idx, end_idx):
    left_idx = pivot_idx + 1
    right_idx = end_idx
    while True:
        # (왼쪽) pivot보다 큰 데이터를 찾을 때까지 반복
        while left_idx < end_idx and array[left_idx] < array[pivot_idx]:
            left_idx += 1
        # (오른쪽) pivot보다 작은 데이터를 찾을 때까지 반복
        while right_idx > pivot_idx and array[right_idx] > array[pivot_idx]:
            right_idx -= 1
        if right_idx <= left_idx:
            break  # 교차하는 경우
        array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        left_idx += 1
        right_idx -= 1

    # 교차하는 경우
    # left_idx와 right_idx가 교차하면 right_idx, left_idx는 pivot을 기준으로 작은 값과 큰 값의 경계에 위치
    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]
    return right_idx

def quick(array, start_idx, end_idx):
    if start_idx < end_idx:
        pivot_idx = partition(array, start_idx, end_idx)
        quick(array, start_idx, pivot_idx-1) 
        quick(array, pivot_idx+1, end_idx)


# Input
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

quick(array, 0, len(array)-1)
print(array)