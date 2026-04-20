class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def delete_node(self, target_data):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        
        if self.head.data == target_data:
            self.head = self.head.next
            return
        
        current_node = self.head
        previous_node = None
        
        while current_node is not None and current_node.data != target_data:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            print(f" '{target_data}' was not found in the list.")
        
        previous_node.next=current_node.next

    def prepend(self, data):
        new_node= Node(data)
        new_node.next = self.head
        self.head = new_node



    def update():
        pass

    def insert():
        pass

    def search():
        pass
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        
        print("None")

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.prepend(15)
linked_list.delete_node(3)
linked_list.display()


