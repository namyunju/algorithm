# 본문 문자열 t 내에 찾고자하는 패턴 p 찾기
# 있으면 인덱스, 없으면 -1 리턴
def brute_force(p,t):
    i = 0 # p 인덱스
    j = 0 # t 인덱스
    M = len(p)
    N = len(t)

    while i < M and j < N:
        if p[i] != t[j]:
            j = j-i
            i = -1
        i = i + 1
        j = j + 1

    # 패턴의 끝까지 다 나왔다면
    if i == M:
        return j - M
    else:
        return -1

'''
p 1 2
t 4 5 1 3 1 2 3
같은 부분을 찾을 때까지
p는 0 인덱스, t는 1씩 인덱스 옮겨가면서 비교

같은 부분 발견 시, p와 t 모두 1씩 인덱스 이동
같다가 달라지면 p는 처음부터 다시, t는 지금 검사 시작점점 다음터 다시 검사 i-j+1

'''

print(brute_force(['a','b'], ['a','c','a','b','d']))
print(brute_force('ab', 'acabd'))