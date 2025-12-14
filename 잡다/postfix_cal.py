'''
후위 연산
6528-*2/+

(6+5*(2-8)/2) = -9

'''

postfix = '6528*2/+'

top = -1
stack = [0]*100

for token in postfix:
    if token not in '+-/*':
        top += 1
        stack[top] = int(token)
    else:
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if token == '+':
            top += 1
            stack[top] = op1 + op2
        elif token == '-':
            top += 1
            stack[top] = op1 - op2
        elif token == '*':
            top += 1
            stack[top] = op1 * op2
        elif token == '/' :
            top += 1
            stack[top] = op1 / op2
print(stack[top])



icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖 연산자 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

def cal_post(postfix):
    stack = []

    for token in postfix:
        # 토큰이 피연산자라면
        if token not in '()+-*/':
            stack.append(int(token))
        # 토큰이 연산자라면, 스택에 쌓인 숫자 두 개 가져와서 연산산
       else:
            right = stack.pop()
            left = stack.pop()

            if token =='-':
                result = left - right
            elif token == '+':
                result = left+ right
            elif token == '*':
                result = left*right
            elif token == '/':
                result = left / right


            stack.append(result)
        
    return stack.pop()