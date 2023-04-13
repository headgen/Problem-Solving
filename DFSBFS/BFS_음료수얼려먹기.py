from collections import deque

# Input
N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()3
    q.append((x, y))
    
    if maps[x][y] == 1:  # 아이스크림을 만들 수 없는 공간이거나 '이미 탐색한 곳'
        return False

    while q:
        curr_x, curr_y = q.popleft()
        maps[curr_x][curr_y] = 1  # 탐색한 곳으로 변경(visited[curr_x][curr_y] = True)

        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            
            if 0 <= next_x < N and 0 <= next_y < M and maps[next_x][next_y] == 0:
                q.append((next_x, next_y))

    # 하나의 아이스크림이 만들어지는 공간을 모두 탐색한 경우에 True
    return True


cnt = 0

for i in range(N):
    for j in range(M):
        if bfs(i, j) == True:
            cnt += 1

print(cnt)