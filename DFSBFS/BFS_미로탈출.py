from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        curr_x, curr_y = q.popleft()

        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and maps[next_x][next_y] == 1:
                maps[next_x][next_y] = maps[curr_x][curr_y] + 1
                q.append((next_x, next_y))
        
    return maps[N-1][M-1]  # 마지막 칸은 항상 1이다.
                

print(bfs(0, 0))