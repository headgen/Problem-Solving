N = int(input())
plans = input().split()

x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            # 예외조건을 위해서 변수를 따로 만듬(nx, ny)
            next_x = x + dx[i]
            next_y = y + dy[i]

    if next_x < 1 or next_x > N or next_y < 1 or next_y > N:
        continue
    x, y = next_x, next_y

print(x, y)
