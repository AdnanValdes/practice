class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        # The head variable points to the HEAD of the LinkedList
        self.head = None

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
        if self.head is None:
            print("List is empty")
            return

        itr = self.get_last_node()
        while itr:
            print(str(itr.data), "-->", end="")
            itr = itr.prev

        print("")

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        self.head = Node(data, next=self.head, prev=None)
        self.head.next.prev = self.head
    

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, next=None, prev=itr)

    def insert_values(self, data_list):
        for value in data_list:
            self.insert_at_end(value)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        count = 0
        index -= 1
        itr = self.head
        while count < index:
            count += 1
            itr = itr.next

        node = Node(data, itr.next, itr)
        itr.next.prev = node
        itr.next = node

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr.data != data_after:
            itr = itr.next
        
        itr.next = Node(data_to_insert, itr.next, itr)

    def remove_by_value(self, data):
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next   
        
if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print_forward()
    # ll.print_backward()
    ll.insert_at_end("figs")

    ll.insert_at(0,"jackfruit")
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.print_backward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
    ll.print_backward()