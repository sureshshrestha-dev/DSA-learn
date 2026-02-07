class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, value):
        if self.is_full():
            return False
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True

    def front(self):
        return -1 if self.is_empty() else self.queue[self.head]

    def rear(self):
        return -1 if self.is_empty() else self.queue[self.tail]

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.k == self.head

if __name__ == "__main__":
    q = CircularQueue(3)
    assert q.enqueue(1) == True
    assert q.enqueue(2) == True
    assert q.enqueue(3) == True
    assert q.enqueue(4) == False
    assert q.rear() == 3
    assert q.is_full() == True
    assert q.dequeue() == True
    assert q.enqueue(4) == True
    assert q.rear() == 4
    print("Circular Queue tests passed!")
