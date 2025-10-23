class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_full(self):
        """Check if the queue is full"""
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front == -1

    def enqueue(self, item):
        """Add an item to the queue"""
        if self.is_full():
            return "Queue is full!"
        elif self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item
        return f"Inserted {item}"

    def dequeue(self):
        """Remove and return the front item"""
        if self.is_empty():
            return "Queue is empty!"
        
        item = self.queue[self.front]
        self.queue[self.front] = None   # Optional: clear the slot
        if self.front == self.rear:     # Only one element left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return f"Removed {item}"

    def display(self):
        """Display the current state of the queue"""
        if self.is_empty():
            return "Queue is empty!"
        
        elements = []
        i = self.front
        while True:
            elements.append(str(self.queue[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return " -> ".join(elements)


# Example Usage:
cq = CircularQueue(3)
print(cq.enqueue(1))
print(cq.enqueue(2))
print(cq.enqueue(3))
print(cq.enqueue(4))  # Should print "Queue is full!"
print(cq.display())
print(cq.dequeue())
print(cq.enqueue(4))
print(cq.display())
