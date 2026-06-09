'''
다익스트라 풀이 209ms
bfs 풀이 144ms

문제의 특수성
간선의 가중치가 0~9로 아주 작은 값

다익스트라에서는 heapq를 이용하기 때문에 추가할 때마다 정렬을 해야 함. ElogV

bfs에서는 가지치기를 통해 최적화
정렬을 안 하는 대신 짧은 거리부터 방문하지 않기 때문에더 작은 값을 찾으면 중복 방문이 가능.
그러나 큐에 넣고 빼는 연산이 O(1)이라 정렬 비용이 없음.

만약 가중치가 훨씬 넓은 범위의 숫자였다면 중복 방문 횟수가 늘어서 다익스트라가 유리
'''
from collections import deque
 
def solve():
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
     
    INF = 999999
    min_cost = [[INF] * N for _ in range(N)]
    min_cost[0][0] = 0
     
    queue = deque([(0, 0)])
     
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
     
    while queue:
        r, c = queue.popleft()
        cur_cost = min_cost[r][c]
         
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
             
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = cur_cost + grid[nr][nc]
                 
                if next_cost < min_cost[nr][nc]:
                    min_cost[nr][nc] = next_cost
                    queue.append((nr, nc))
    return min_cost[N-1][N-1]
 
T = int(input())
for tc in range(1, T+1):
    result = solve()
    print(f'#{tc} {result}')