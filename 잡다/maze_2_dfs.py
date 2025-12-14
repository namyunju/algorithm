# 재귀 호출 버전
# 현위치 입력 시 목적지 도달 여부 반환

# 스택을 직접 만들어서 쓰느냐
# 파이썬이 만들게 하느냐의 차이
# 스택 말고 함수 호출에 지난 경로를 저장
def DFS2(si,sj):

    # 재귀호출은 함수를 반복해서 호출
    # visited를 함수 내에 적으면 매번 초기화됨 >> 함수 밖으로
    # visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1

    # return 이 어렵다면 answer 전역 변수 이용
    # global answer
    # return 1 대신 answer = 1

    if maze[si][sj] == 3:
        return 1
    else:
        for di, dj in [[-1,0], [0,1],[0,-1],[1,0]]:
            ni, nj = si + di, sj + dj
            if 0<= ni <N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                if DFS2(ni,nj):
                    return 1
        else:
            return 0









T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
    print(f'#{tc} {DFS2(si,sj)}')


    # answer = 0
