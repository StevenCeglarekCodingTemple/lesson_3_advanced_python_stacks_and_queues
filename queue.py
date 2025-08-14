class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None   # Front of queue (next item to be removed)
        self.tail = None   # Rear of queue (last item added)  
        self.size_count = 0
    
    def is_empty(self):
        """Check if queue has no elements"""
        return self.head is None
    
    def enqueue(self, item):
        """
        Add item to rear of queue (tail)
        
        Args:
            item: Data to add to the queue
        
        Hint: This is very similar to stack push, but we add to tail!
        """
        new_node = Node(item)
        
        if self.is_empty():
            # First node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Add to tail (rear of queue) - just like stack push
            self.tail.next = new_node
            self.tail = new_node
        
        self.size_count += 1
        print(f"Enqueued: {item}")
        
    
    def dequeue(self):
        """
        Remove and return front item (head) - O(1) operation!
        
        Returns:
            The data from the front of the queue
        
        Raises:
            IndexError: If queue is empty
        
        """
        # YOUR IMPLEMENTATION HERE
        
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")

        item = self.head.data
        self.head = self.head.next
        
        # If queue becomes empty, reset tail
        if self.head is None:
            self.tail = None
        
        self.size_count -= 1
        print(f"Dequeued {item}")
        return item
    
    def front(self):
        """
        View front item without removing it
        
        Returns:
            The data from the front item
        
        """
        # YOUR IMPLEMENTATION HERE
        
        if self.is_empty():
            raise IndexError("Cannot view front if queue is empty")
        return self.head.data
        
    def rear(self):
        """
        View rear item without removing it
        
        Returns:
            The data from the rear item
        
        """
        # YOUR IMPLEMENTATION HERE
        
        if self.is_empty():
            raise IndexError("Cannot view rear if queue is empty")
        return self.tail.data

    def size(self):
        """Get number of items in queue"""
        return self.size_count
    

#  Test your queue implementation
def test_queue():
    """Test function to verify your Queue implementation"""
    print("=== Testing Queue Implementation ===\n")
    
    queue = Queue()
    print(f"Is empty? {queue.is_empty()}")
    
    # Test enqueue
    print("\n1. Testing enqueue:")
    queue.enqueue("first")
    queue.enqueue("second") 
    queue.enqueue("third")
    
    print(f"Queue size: {queue.size()}")
    print(f"Front item: {queue.front()}")
    print(f"Rear item: {queue.rear()}")
    
    # Test dequeue
    print("\n2. Testing dequeue (FIFO order):")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"Queue size now: {queue.size()}")
    
    # Test edge cases
    print("\n3. Testing edge cases:")
    try:
        queue.dequeue()  # Should raise error
    except IndexError as e:
        print(f"Correctly caught error: {e}")
    
    print("\nTest completed!")

# Uncomment to test your implementation
 
test_queue()