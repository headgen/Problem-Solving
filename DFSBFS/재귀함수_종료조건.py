def recursive_function(i):
    # 종료 조건 명시
    if i == 5:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.') # Stack Frame

recursive_function(1)