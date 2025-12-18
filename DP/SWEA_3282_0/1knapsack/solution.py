'''
K 이하의 부피 최대 가치 물건 담기

동일 부피 최대 가치를 담는 dp를 이용

한 아이템 부피가 v, 가치가 c 일 때,
이 아이템을 넣는 경우와 안 넣는 경우 가치를 비교하여 업데이트


예를 들어 가방 부피 10
부피가 3인 물건을 넣을지 말지 고민
- 부피가 7일 때 현재 가치 + 아이템 가치 vs 부피 10 가치
- 부피가 6일 때 현재 가치 + 아이템 가치 vs 부피 9 가치
...
뒤에서부터 업데이트

주의
앞에서부터 업데이트하면 동일 아이템 여러 번 넣게 될 수 있음

(부피가 큰 경우부터 하면 작은 경우에 영향을 주지 않지만,
부피가 작은 경우부터 하면 부피가 큰 경우에 영향을 줌)
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    items = []
    for _ in range(N):
        items.append(list(map(int, input().split())))
    dp = [0]*(K+1)
     
    for v, c in items:
        for j in range(K, v-1, -1):
            if dp[j] < dp[j-v]+c:
                dp[j] = dp[j-v]+c
    print(f"#{tc} {dp[K]}")