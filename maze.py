# 2차원
# 시작점 입력 시
def DFS(si, sj):
    # 2차원 배열 방문 여부 기록용
    visited = [[0] * N for _ in range(N)]
    # 이전 위치
    stack = []

    # 현재 탐색 위치
    vi, vj = si, sj
    visited[vi][vj] = 1
    # 미로 이동 방향
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while True:
        # 목표 지점
        # return으로 함수 종료
        if maze[vi][vj] == 3:
            return 1

        for d in range(4):
            ni = vi + di[d]
            nj = vj + dj[d]
            # 이동 가능성
            # 유효 인덱스, 길, 방문 기록
            if ((0 <= ni < N and 0 <= nj < N) and (maze[ni][nj] != 1) and (not visited[ni][nj])):
                # 조건 만족 시 이동
                # 현 위치 stack 에 저장 / visited / 현위치 변경
                stack.append((vi, vj))
                visited[ni][nj] = 1
                vi, vj = ni, nj
                print((vi,vj))
                # 가려는 방향 선정 시, 다른 방향은 무시
                break
        # for-else
        # 네 방향 중 가능한 경우 없음
        else:
            if stack:
                # 이전 위치 좌표. 두 요소로 구성되어 있으므로
                vi, vj = stack.pop()
            else:
                break
    # 탐색 모두 마쳤으나 목적지 찾지 못함
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
    print(f'#{tc} {DFS(si,sj)}')

'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''
'''
#1 1
#2 1
#3 0

'''