
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # this operation insert items at the end of the linked list
    # so we have to maniplate the tail node in O(1) running time
    def insert(self, data):

        new_node = Node(data)

        # When the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else: 
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # we can traverse a doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous



if __name__ == '__main__':

    listed_list = DoublyLinkedList()
    listed_list.insert(1)
    listed_list.insert(2)
    listed_list.insert(3)

    print(5*"-")
    listed_list.traverse_forward()

    print(5*"-")
    listed_list.traverse_backward()


        
