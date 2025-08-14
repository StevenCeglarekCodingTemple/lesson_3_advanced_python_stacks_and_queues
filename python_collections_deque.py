from collections import deque

# Create an efficient queue
queue = deque()

# Enqueue operations (add to rear)
queue.append("first")   # Enqueue
queue.append("second")  # Enqueue
queue.append("third")   # Enqueue

print(f"Queue: {list(queue)}") # ["first", "second", "third"]
print(f"Front item: {queue[0]}") # Peek at front: first

# Dequeue operations (remove from front)
front_item = queue.popleft()  # Dequeue returns 'first'
print(f"Dequeued: {front_item}")
print(f"Queue after dequeue: {list(queue)}") # ["second", "third"]

# Check if empty
is_empty = len(queue) == 0
print(f"Is empty: {is_empty}")


# Key Queue Operations with deque:

# Enqueue: deque.append(item)
# Dequeue: deque.popleft()
# Peek Front: deque[0]
# Is Empty: len(deque) == 0
# Size: len(deque)