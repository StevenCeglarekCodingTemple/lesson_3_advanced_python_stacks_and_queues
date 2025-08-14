from linked_list import Node, LinkedList

class Task:
    def __init__(self, name):
        self.name = name           # Task description (string)
        self.complete = "incomplete"  # Status: "complete" or "incomplete"
        
    def add_task(self):
        # Create a new Task object
        # Add it to the linked list using the append method
        # Provide user feedback
