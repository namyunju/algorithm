import heapq
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def solve():
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
     
    INF = float('inf')
    min_cost = [[INF]*N for _ in range(N)]
    min_cost[0][0] = 0
     
    pq = []
    heapq.heappush(pq, (0, 0, 0))
     
    while pq:
        cur_cost, r, c = heapq.heappop(pq)
         
        if r == N-1 and c == N-1:
            return cur_cost
         
        if cur_cost > min_cost[r][c]:
            continue
            
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = cur_cost + board[nr][nc]
                if next_cost < min_cost[nr][nc]:
                    min_cost[nr][nc] = next_cost
                    heapq.heappush(pq, (next_cost, nr, nc))
 
T = int(input())
for tc in range(1, T+1):
    result = solve()
    print(f'#{tc} {result}')