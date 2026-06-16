class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.front = 0
        self.rear = -1

    def enqueue(self, data):
        if self.rear == self.capacity - 1:
            print("Queue Overflow!")
            return
        self.rear += 1
        self.queue[self.rear] = data
        print(f"{data} enqueued (pushed) to queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return -1
        data = self.queue[self.front]
        self.front += 1
        return data

    def peek_front(self):
        if self.is_empty():
            print("Queue is Empty!")
            return -1
        return self.queue[self.front]

    def is_empty(self):
        return self.front > self.rear

    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        print("Queue Elements (Front to Rear): ", end="")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:", q.dequeue())
q.display()
print("Front element:", q.peek_front())