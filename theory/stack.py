stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()

stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # Stack 거꾸로 뒤집기
print(stack)