
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        # this is the first node of the linked list
        # WE CAN ACCESS THIS NODE EXLUSIVELY!!!

        self.head = None
        self.num_of_nodes = 0

    # O(1) Time Complexity
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        
        if self.head is None: # the head is NULL ( so the data struture is empty)
            self.head = new_node
        
        else: # if the linked list is not empty
            new_node.next_node = self.head # we hav eto update the references
            self.head = new_node

    # O(N) Time Complexity
    def insert_end(self, data):

        self.num_of_nodes += 1
        new_node = Node(data)

        
        if self.head is None: # the head is NULL ( so the data struture is empty)
            self.head = new_node

        else: # if the linked list is not empty
            actual_node = self.head
            
            # this is why linked list is O(N)
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # actual_node is the last node: so we insert the new_node
            # right after the actual node
            actual_node.next_node = new_node

    def size_of_list(self):
        return self.num_of_nodes
    
    def traverse(self):

        """
        print all the nodes in the linked list
        """
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    # O(N) linear runnig time
    def remove(self, data):
        
        if self.head is None:
            return
        
        actual_node = self.head
        # we have to track the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous node 
        previous_node = None

        # search for the itme we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return
        
        # update the references (so we have the data we want to remove)
        # the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node
            previous_node.next_node = actual_node.next_node # need to upate the reference for the previous node to the next node



if __name__ == '__main__':

    linked_list = LinkedList()

    ## add items to the begining of the linked list
    linked_list.insert_start(10)
    linked_list.insert_start("Adam")
    linked_list.insert_start(7.5)

    ## add items to the end of the linked list
    linked_list.insert_end(100)
    linked_list.insert_end(1000)

    linked_list.traverse()

    print(5*"-")

    ## remove items from the linked list
    linked_list.remove(10) # this item doesn't exist in the linked list
    linked_list.traverse()
    print(5*"-")

    linked_list.remove("Adam") # this itme exist in the linked list
    linked_list.traverse()

