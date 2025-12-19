T = 10
 
def multi(N,M,now):
    if M == 0:
        return now
 
    return multi(N,M-1,now*N)
 
 
for _ in range(T):
    tc = int(input())
    N, M = map(int, input().split())
    ans = multi(N,M,1)
    print(f"#{tc} {ans}")