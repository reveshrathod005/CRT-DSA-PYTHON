# Linked List Insert at Beginning and End

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


list_ = MyLinkedList()
list_.insert_at_beginning(10)
list_.insert_at_beginning(20)
list_.insert_at_beginning(30)
list_.display()
list_.insert_at_end(40)
list_.insert_at_end(50)
list_.display()

