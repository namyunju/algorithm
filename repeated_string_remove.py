# 동일한 문자가 연속 2회 나오는 순간 삭제
# 붙인 문자에서도 반복
# 남은 문자열의 길이 출력

# 리스트와 인덱스, 문자열 길이
#
# stack 에 하나씩 쌓기
# 새로 넣는 게 같으면 앞서 있는 애를 없애

T = int(input())
for tc in range(1, T + 1):
    text = list(input())
    N = len(text)

    stack = []
    stack.append(text[0])
    top = 0

    for i in range(1, N):
        if top != -1 and stack[top] == text[i]:
            stack.pop()
            top -= 1

        else:
            stack.append(text[i])
            top += 1

    print(f'#{tc} {len(stack)}')



