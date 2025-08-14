# Example 1: Function call tracking (Stack Behavior)
def process_nested_data(data):
    call_stack = []  # Use list as a stack
    
    def helper(current_data, depth):
        call_stack.append(f"Processing level {depth}")
        print(f"Call Stack: {call_stack}")

        # Process data...
        if isinstance(current_data, list):
            for item in current_data:
                helper(item, depth + 1)

        call_stack.pop()  # Return from this level

    helper(data, 0)


# Example 2: Task Processing (Queue Behavior)
def process_tasks():
    from collections import deque
    task_queue = deque()
    
    # Add tasks
    task_queue.append("Send email")
    task_queue.append("Update code")
    task_queue.append("Generate a report")

    # Process tasks in order
    while task_queue:
        current_task = task_queue.popleft()
        print(f"Processing: {current_task}")
        # Do the task