'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# V 정점의 개수
# E 간선의 개수
V, E = map(int, input().split())

# 정점들의 연결 정보가 입력으로 들어온다
graph = list(map(int,input().split()))

# 인접 행렬
# 어떤 정점 x와 어떤 정점 y가 연결 되어있는지 여부
# True(1) 와 False(0) 로 나타냄
# True(1) 이라면 연결되어 있음. x -> y 간선 존재
# adjM[x][y] = True 또는 adjM[x][y] = 1
# False(0)이라면 연결 안 되어 있음. x->y 간선 없다.
# adjM[x][y] = False 또는 adjM[x][y] = 0

adjM = [[0]*(V+1) for _ in range(V+1)]

# 간선 번호 i
for i in range(E):
    # s 정점과 e 정점은 연결되어 있다.(인접해있다.)
    s, e = graph[i*2], graph[i*2+1]

    # s정점에서 e정점으로 가는 간선이 있다.(아래는 무향 그래프의 경우만)
    adjM[s][e] = 1
    adjM[e][s] = 1

# s: 탐색을 시작하는 정점 번호
# N: 정점의 개수(마지막 정점 번호)
def DFS(s, N):
    # 깊이 우선 탐색( 한 방향씩 가능한 깊게 탐색)
    # 방문한 정점으로 돌아온다. 탐색한 길은 재탐색X
    visited = [0] *(N+1)
    # x번을 탐색한 적 있다. -> visited[x] = 1
    # y번 탐색한 적 없다 -> visited[y] = 0

    # 가장 마지막에 방문했던 정점으로 쉽게 돌아가기 위해 스택 사용 (pop())
    stack = []

    # 현재 탐색중인 정점 번호
    v = s
    # 시작 정점 방문했다고 체크 -> 1로 바꿈
    visited[s] = 1
    print(v, end = " ")

    while True:
        # 현재 정점 v에서 탐색. v에서 갈 수 있는 다른 정점
        # nv : 다른 정점 번호
        for nv in range(1, V+1):
            # 갈 수 있는 nv는
            # 첫 째, v와 nv 인접 / 둘 째, nv 이전에 방문한 적 없음
            if adjM[v][nv] and not visited[nv]:
                # v를 stack 에 저장하고 nv 로 이동
                stack.append(v)

                v = nv

                visited[nv] = 1
                print(nv, end = " ")
                # nv 로 이동 했으니 다른 이동 가능 정점은 찾지 않아도 됨
                break
        # for - else
        else:
            # 중간에 break 한 적 없으면 실행되는 코드
            # break 한 적 없다 -> 갈 수 있는 다른 정점 찾지 못했다. -> 이전 위치로
            # stack의 top이 직전 위치
            # 꺼내기 전에 비어있지 않은가 확인

            if stack:
                # 비어있지 않으면 돌아갈 곳 있음
                

            # stack이 비어있다? 끝
            else:
                break

