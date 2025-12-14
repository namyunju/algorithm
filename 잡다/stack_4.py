T = int(input())
for tc in range(1, T + 1):
    text = input()
    N = len(text)

    pair = {'(': ')', '{': '}'}

    ans = 1
    top = -1
    stack = [0] * N

    for x in text:
        if x in ['(', '{']:
            top += 1
            stack[top] = x

        elif x in [')', '}']:
            if top == -1:
                ans = 0
                break

            else:
                top -= 1
                y = stack[top + 1]
                if x != pair[y]:
                    ans = 0
                    break
    if top != -1:
        ans = 0

    print(f'#{tc} {ans}')


