# stack은 후입 선출
# 파이썬에서 append와 pop 사용하지만 리스트처럼 중간 인덱스 값에 수정을 가하면 안 됨

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

