class Node:
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None # Top of stack (most recently added)
        self.tail = None # Bottom of stack (first item added)
        self.size_count = 0
        
    def is_empty(self):
        """Check if stack has no elements"""
        return self.head is None
    
    def push(self, item):
        """Add item to top of stack (head)"""
        new_node = Node(item)
        
        if self.is_empty():
            # First node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Add to head (top of stack)
            new_node.next = self.head
            self.head = new_node
            
        self.size_count += 1
        print(f"Pushed {item} onto stack")
        
    def pop(self):
        """Remove and return top item (head)"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        
        item = self.head.data
        self.head = self.head.next
        
        # If stack becomes empty, reset tail
        if self.head is None:
            self.tail = None
            
        self.size_count -= 1
        print(f"Popped {item} from stack")
        return item
    
    def peek(self):
        """View top item without removing it"""
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        return self.head.data

    def size(self):
        """Get number of items in stack"""
        return self.size_count
    
stack = Stack()
print(f"Is empty? {stack.is_empty()}")

# Push some items
stack.push("first")
stack.push("second")
stack.push("third")

# Peek at top
print(f"Top item: {stack.peek()}")
print(f"Stack size: {stack.size()}")

# Pop items
while not stack.is_empty():
    item = stack.pop()
    print(f"This item was popped: {item}")
    print(f"Stack size is now: {stack.size()}")
    