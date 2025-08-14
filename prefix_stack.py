'''
중위 > 후위
(6+5*(2-8)/2)
6528-*2/+
'''
#
# stack = [0]*100
# top = -1
#
icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖 연산자 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

# infix = '(6+5*(2-8)/2)'
# postfix = ''
#
# for token in infix:
#     if token not in '(+-*/)':
#         postfix += token
#     elif token == ')':
#         while top >-1 and stack[top] != '(':
#             top -= 1
#             postfix += stack[top+1]
#         if top != -1:
#             top -= 1    # '('를 버림
#     else:
#         if top == -1 or isp[stack[top]] < icp[token]:  # 토큰의 우선순위가 더 높으면
#             top += 1  # push
#             stack[top] = token
#         elif isp[stack[top]] >= icp[token]:
#             while top > -1 and isp[stack[top]] >= icp[token]:
#                 postfix += stack[top]
#                 top -= 1
#             top += 1  # push
#             stack[top] = token
# print(postfix)



# 중위를 후위로 함수
def get_postfix(infix):
    postfix = ''

    stack = []

    for token in infix:
        # 피연산자라면 그대로 써줌
        if token not in '()+-*/':
            postfix += token
        # 연산자일 때
        else:
            # infix 의 토큰이 닫는 괄호라면 '(' 나올 때까지
            # stack 에 있는 모든 연산자를 profix로 뽑아냄
            if token == ')':
                while stack:
                    operator = stack.pop()
                    if operator == '(':
                        break
                    postfix += operator
            # 닫는 괄호 아니라면
            # stack 의 연산자와 현재 infix의 token의 우선순위를 비교
            # 토큰이 더 높으면 stack 에 넣고
            # 토큰이 이하라면 토큰보다 낮은 연산자 나올 때까지 pop
            else:
                while stack and icp[token] <= isp[stack[-1]]:
                    postfix += stack.pop()
                stack.append(token)

    while stack:
        postfix += stack.pop()

    return postfix
print(get_postfix('(6+5*(2-8)/2)'))