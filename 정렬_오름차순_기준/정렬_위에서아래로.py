'''입력으로 주어진 수열을 내림차순으로 정렬'''

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort(reverse=True)
for element in array:
    print(element, end = ' ')