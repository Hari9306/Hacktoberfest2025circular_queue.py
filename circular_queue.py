class CircularQueue:
    def _init_(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return "Full"
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        return "Inserted"  # ✅ Return confirmation

    def dequeue(self):
        if self.front == -1:
            return "Empty"
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.enqueue(4))
