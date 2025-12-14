# memo를 위한 배열 할당. 모두 0으로 초기화
# memo[0] 을 0으로 memo[1]은 1로 초기화

# 기존 피보나치
# 인덱스 0 1 2 3 4 5 6 7
# 수열   0 1 1 2 3 5 8 13
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# 메모이제이션 이용
# memo로 피보나치 값을 저장
# 매번 fibo 함수를 호출하지 않고 저장해두었던 값을 이용
# 함수 밖에  memo라는 리스트 생성(사전준비 필요)
def fibo1(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]


memo = [0] * (6+1)
memo[0] = 0
memo[1] = 1

# 동적계획법 DP로 구현한 피보나치 코드
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]




print(fibo(6)) #
print(fibo1(6)) # 1 1 2 3 5 8