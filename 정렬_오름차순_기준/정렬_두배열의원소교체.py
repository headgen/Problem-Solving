N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        B[i], A[i] = A[i], B[i]
    else:
        break  # A의 원소가 더 크거나 같으면 swap이 무의미해지므로 반복문 탈출

print(sum(A))