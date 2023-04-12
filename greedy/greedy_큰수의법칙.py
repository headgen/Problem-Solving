# N: 배열의 크기, M: 숫자가 더해지는 총 횟수, K: 똑같은 수가 최대 나올 수 있는 횟수
N, M, K = map(int, input().split())

# 배열 입력
nums = list(map(int, input().split()))
nums.sort() # 오름차순(작은 수부터 큰 수)

first = nums[-1]
second = nums[-2]

answer = 0

while True:
    for i in range(K):
        if M == 0:
            break
    # 더할 때마다 M의 횟수를 차감하는 것이 포인트
        answer += first
        M -= 1
        
    if M == 0:
        break
    answer += second
    M -= 1

print(answer)
