# 괄호 짝 검사 프로그램

txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    # txt에 ( 가 있다면, 0층에 ( 를 저장
    if x == '(':
        top += 1
        stack[top] = x

    # txt에 ) 가 있다면 2가지 경우. 앞에 ( 가 있을 때와와 없을 때
    elif x == ')':
        # 앞서 여는 괄호 없었다면 중단
        # 즉 ( 가 없는데 ) 가 나왔다면
        if top == -1:
            ans = 0
            break

        # 여는 괄호 하나 버림
        else:
            top -= 1

# text를 다 돌았는데 ( 가 남아있다면
# 즉 ( 와 ) 쌍이 안 맞았다면
if top != -1:
    ans = 0

print(ans)


# 3가지 괄호 모두 등장 시
# 짝짓는 딕셔너리
pair = {'(':')', '{':'}', '[':']'}
for x in txt:
    if x in ['(','{','[']:
        top += 1
        stack[top] = x
    elif x in [')', '}', ']']:
        if top == -1:
            ans = 0
            break
        else:
            top -= 1
            y = stack[top+1]
