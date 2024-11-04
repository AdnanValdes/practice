class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        while itr:
            print(str(itr.data), "--> ", end="")
            itr = itr.next
        print("")
    
    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def insert_values(self, data_list):
        for value in data_list:
            self.insert_at_end(value)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index <= 0 or index >= self.get_length():
            raise IndexError

        if index == 0:
            self.head = self.head.next
            return
        

        index -= 1
        count = 0
        itr = self.head
        while count < index:
            count += 1
            itr = itr.next
        
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length() + 1:
            raise IndexError

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length() + 1:
            self.insert_at_end(data)
            return

        count = 0
        index -= 1
        itr = self.head
        while count < index:
            count += 1
            itr = itr.next

        itr.next = Node(data, itr.next)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr.data != data_after:
            itr = itr.next
        
        itr.next = Node(data_to_insert, itr.next)

    def remove_by_value(self, data):
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next   


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_beginning(0)
    ll.print()


    ll2 = LinkedList()
    ll2.insert_values(["banana","mango","grapes","orange"])
    ll2.print()
    print(ll2.get_length())
    ll2.remove_at(1)
    ll2.print()
    ll2.insert_at(1, "piano")
    ll2.insert_after_value("grapes","apple") 
    ll2.remove_by_value("orange")
    ll2.print()
