class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # The head variable points to the HEAD of the LinkedList
        self.head = None

    def print(self):
        """
        Traverses through LinkedList and prints each item
        """

        if self.head is None:
            print("LinkedList is empty")
            return
        # Create something to interate over, starts assign to current HEAD
        itr = self.head
        llstr = ""  # A string to append each value we find

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_begining(self, data):
        """
        Takes a data value and inserts it at beginning of LinkedList
        """
        # Creates a new Node with data, and points at the current HEAD
        node = Node(data, self.head)
        # Then updates the HEAD of the list to point at the Node just created
        self.head = node

    def insert_at_end(self, data):
        """
        Inserts a data value at the end of current LinkedList
        """

        # if the head is none, the last node is the node we are creating
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """
        Creates a new LinkedList from a set of values
        """
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            # Need to stop at element _prior_ to the one we have to delete in order to update link
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)

        if index == self.get_length():
            self.insert_at_end(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
                


    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
