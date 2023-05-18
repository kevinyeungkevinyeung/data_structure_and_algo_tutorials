
"""
The task is to find the middle node of a linked list without the need for extra memory (so we are after an in-place algorithm)

1. Naive Solution
    we iterate through the list and count how many elemnts there are in total

    Then traverse the list again and the node with index count/2 is the middle node

2. Using two pointer:
    We can use two pointers to get the middle node in O(N)

    first pointer: traverse the linked list one node at a time
    second pointer: traverse the linked list two nodes at a time

    when the fast pointer reaches the end of the list then the slower pointer is pointing to the middle node
"""