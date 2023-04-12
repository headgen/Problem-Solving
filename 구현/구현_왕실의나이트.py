location = input()
row = int(location[1])
# 아스키 코드 사용
col = ord(location[0]) - ord('a') + 1  # 1을 더해야 되는거 주의

steps = [(-2, -1), (2, -1), (-2, 1), (2, 1), (1, 2),
          (-1, 2), (1, -2), (-1, -2)]

cnt = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        cnt += 1

print(cnt)