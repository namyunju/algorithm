# V 개 이내 노드 E개 간선
# 방향성 그래프
# 두 노드 경로 존재 여부

# 시작점과 끝 점 입력 시 도달 여부
def DFS(s, e):
    stack = []
    # 전체 노드 개수 V
    visited = [0] * (V + 1)
    # 스택에 현 위치 넣고 이동 시작
    stack.append(s)

    # 스택이 빌 때까지
    while stack:
        now = stack.pop()
        visited[now] = 1

        for move in range(1, V + 1):
            if not visited[move] and adjL[now][move]:
                stack.append(move)

    if visited[e]:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adjL = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())

        adjL[s][e] = 1

    S, G = map(int, input().split())

    print(f'#{tc} {DFS(S, G)}')



