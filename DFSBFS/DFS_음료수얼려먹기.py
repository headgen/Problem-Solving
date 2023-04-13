# Input
N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(curr_x, curr_y):
    maps[curr_x][curr_y] = 1  # 현 노드 방문 처리

    for i in range(4):
        next_x = curr_x + dx[i]
        next_y = curr_y + dy[i]

    
        if 0 <= next_x < N and 0 <= next_y < M and maps[next_x][next_y] == 0:
            dfs(next_x, next_y)
        
    


cnt = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            cnt += 1
            dfs(i, j)

print(cnt)