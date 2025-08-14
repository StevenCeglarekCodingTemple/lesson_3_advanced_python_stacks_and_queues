# Using Python list as a stack

stack = []

# Push operations (add to the top)
stack.append("first")  # Push
stack.append("second") # Push
stack.append("third")  # Push

print(f"Stack: {stack}")   # ["first", "second", "third"]
print(f"Top item: {stack[-1]}")  # third (Peek at the top of the list (stack))

# Pop operations (remove from top)
top_item = stack.pop() # Pop returns 'third'
print(f"Popped: {top_item}") 
print(f"Stack after pop: {stack}")  # ["first", "second"]

# Check if empty
is_empty = len(stack) == 0
print(f"Is empty: {is_empty}")

# Key Stack Operations with Python Lists:

# Push: list.append(item)
# Pop: list.pop()
# Peek: list[-1]
# Is Empty: len(list) == 0
# Size: len(list)