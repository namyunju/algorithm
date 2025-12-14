# 0에서 99로 갈 수 있는가 여부
# 테스트 케이스와 길의 개수 주어짐
# 각 경로 주어짐


# 시작점을 입력하면 시작점에서 이동가능한 점들 파악
# 그 점들 중 하나씩 방문 여부 파악 후 방문 안 했다면
# 그 점에 대하여 같은 작업을 반복
# 이어진 길이 있는 모든 점에 방문 했음을 기록

# 즉, 시작점을 넣으면 가능한 모든 방문 지점을 기록하는 함수
def dfs(s):
    visited[s] = 1
    next_visits = graph[s]
    # 깊이 탐색
    for next_visit in next_visits:
        if not visited[next_visit]:
            dfs(next_visit)


for _ in range(1, 11):

    tc, E = map(int, input().split())

    visited = [0] * 100

    # E 개의 경로 정보 ( 2E 개의 원소, 두 개씩 묶어야 함)
    lst = list(map(int, input().split()))

    # lst를 보고 가능경로를 저장
    # graph의 인덱스가 출발점, 해당 인덱스의 리스트의 원소가 이동 가능 지점들
    graph = list([] for _ in range(100))
    for i in range(E):
        graph[lst[2 * i]].append(lst[2 * i + 1])

    dfs(0)
    print(f'#{tc} {visited[99]}')