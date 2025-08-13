# 인덱스 i 배열의 길이 N 찾는 값 v
def f(i, N, v):
    arr = list(input())

    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f(i+1, N, v)

print(f(0, 5, 2))