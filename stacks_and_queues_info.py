# Stacks (LIFO) Last In First Out are everywhere:

# Function call management - how programming languages track function calls
# Undo operations - text editors, photo editing, version control
# Expression evaluation - how calculators process mathematical expressions
# Memory management - stack frames in program execution
# Browser navigation - back/forward button implementation

# Queues (FIFO) First In First Out are everywhere:

# Print job management - documents print in order received
# CPU task scheduling - operating system manages process execution
# Breadth-First Search - graph traversal algorithms
# Network packet handling - routers process data packets in order
# Customer service systems - "first come, first served"

# Use Stacks when:

# Need to reverse order of operations
# Implementing undo functionality
# Managing nested structures (function calls, parentheses)
# Depth-first exploration (DFS)

# Use Queues when:

# Processing items in order received
# Implementing waiting lists or scheduling
# Breadth-first exploration (BFS)
# Buffering data streams

# Stack Operation Complexity

# Operation	    Stack	            Time Complexity	  Space Complexity

# push(item)	Add to tail	            O(1)	             O(1)
# pop()	        Remove from tail	    O(1)	             O(1)
# peek()	    View tail data	        O(1)	             O(1)
# is_empty()	Check if head is None	O(1)	             O(1)



# Operation	        Queue	         Time Complexity
# enqueue(item)	  Add to tail	          O(1)
# dequeue()	      Remove from head	      O(1)
# front()	      View head data	      O(1)
# is_empty()	  Check if head is None	  O(1)



