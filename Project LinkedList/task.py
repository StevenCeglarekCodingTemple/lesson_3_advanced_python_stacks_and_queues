from linked_list import Node, LinkedList

class Task:
    def __init__(self, name):
        self.name = name           # Task description (string)
        self.complete = "incomplete"  # Status: "complete" or "incomplete"
        
class ToDoList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.task_list = LinkedList()
        
    def add_task(self, task_name):
        new_task = Task(task_name)
        self.task_list.append(new_task)
        print(f"Added task: '{new_task.name}'")



def test_todo_list():
    todo = ToDoList("My tasks for the day")
    
    task1 = 'Go to the store'
    task2 = 'Walk the dog'
    
    todo.add_task(task1)
    todo.add_task(task2)
    
test_todo_list()