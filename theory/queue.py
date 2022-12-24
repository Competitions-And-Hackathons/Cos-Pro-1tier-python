from collections import deque # 큐는 별도의 패키지 필요

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

queue.append(1)
queue.append(4)
queue.popleft()

print(queue) 
queue.reverse() # Queue 거꾸로 뒤집기
print(queue)