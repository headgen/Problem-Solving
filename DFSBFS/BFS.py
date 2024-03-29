'''
BFS(Breadth-First Search)는 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
BFS는 큐 자료구조를 이용하며, 구체적인 동작과정은 다음과 같습니다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 "모두" 큐에 삽입하고 방문 처리합니다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
'''

from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True  # 현재 노드 방문 처리
    
    # queue가 빌 때까지 반복
    while q:
        v = q.popleft()  # queue에서 하나의 원소를 뽑아 출력
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited[i]:  # 아직 방문하지 않은 인접한 원소들을 queue에 삽입
                q.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * (8 + 1)

bfs(graph, 1, visited)