def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = []

    for k in range(N):
        lst = []
        for r in range(0,k+1):
            lst.append(factorial(k)/(factorial(k-r)*factorial(r)))
        result.append(lst)


    print(result)
