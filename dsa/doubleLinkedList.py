class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        # The head variable points to the HEAD of the LinkedList
        self.head = None
        # The tail varaible points to the TAIL of the LinkedList
        self.tail = None

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("List is empty")
            return
        
        itr = self.head
        while itr:
            print(str(itr.data), "-->", end="")
            itr = itr.next
        
        print("")

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        itr = self.get_last_node()

        if self.head is None:
            print("List is empty")
            return

        print("Reversed linked list:")
        while itr:
            print(str(itr.data), "-->", end="")
            itr = itr.prev

        print("")

    def get_last_node():
        itr = self.head
        while itr:
            itr = self.next
        
        return itr

    def get_length():
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, next=self.head)
        
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node    
            self.head = node

    def insert_at_end(self, data):
        last_node = self.get_last_node()
        last_node.next = Node(data, prev=last_node)

    def insert_at(self, index, data):
        
if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()