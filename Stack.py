class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if len(self.stack) >= self.capacity:
            print("Stack is full!")
        else:
            self.stack.append(value)
            print(f"{value} pushed to stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
            return -1
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
            return -1
        return self.stack[-1]

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print("Stack:", self.stack[::-1])


capacity = int(input("Enter stack capacity: "))
s = Stack(capacity)
running = True

while running:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element to push: "))
        s.push(value)
    elif choice == 2:
        popped = s.pop()
        if popped != -1:
            print("Popped element:", popped)
    elif choice == 3:
        top_element = s.peek()
        if top_element != -1:
            print("Top element is:", top_element)
    elif choice == 4:
        s.display()
    elif choice == 5:
        running = False
        print("Exiting application.")
    else:
        print("Invalid choice! Please select between 1 and 5.")