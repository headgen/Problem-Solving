N, M = map(int, input().split())

min_list = []
for i in range(N):
    nums = list(map(int, input().split()))
    min_list.append(min(nums))

print(max(min_list))