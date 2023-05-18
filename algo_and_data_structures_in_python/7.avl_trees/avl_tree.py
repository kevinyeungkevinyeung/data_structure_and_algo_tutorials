class Node:

    def __init__(self, data, parent):

        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLTree:

    def __init__(self):

        # we can accesss the root node exclusively
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.node)

    def remove_node(self, data, node):

        if node is None:
            return
        
        if data < node.data: # we know the item will be located in left subtree
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we have found the node we want to remove
            #! case 1:) if the node is leaf node
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node", node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

                # after every removal WE hHAVE TO CHECK whether the AVL properties are violated
                self.handle_violation(parent)

            #! when there is a single child
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with single right child")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node

                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent
                
                del node

                # after every removal WE hHAVE TO CHECK whether the AVL properties are violated
                self.handle_violation(parent)

            elif node.right_node is None and node.left_node is not None:
                print("removing a node with single left child...")
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node

                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

                # after every removal WE hHAVE TO CHECK whether the AVL properties are violated
                self.handle_violation(parent)

            #! removing a node with two children
            else:
                print('Removing node with two children....')
                predecessor = self.get_predecessor(node.left_node)

                #swap the node and predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)

        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        
        # we have to consider the left subtree
        if data < node.data:
            # we have to cehck if the left node is a None
            # when the left child is not a None
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)

                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1 

        else:
            # we have to cehck if the left node is a None
            # when the left child is not a None
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1 

        # after every insert WE HAVE TO CHECK whether the AVL properties are violated

        self.handle_violation(node)

    def calc_height(self, node):

        # this is when the node is NULL
        if node is None:
            return -1
        
        else:
            return node.height
        

    def calculate_balance(self, node):

        if node is None:
            return 0
        else:
            return self.calc_height(node.left_node) - self.calc_height(node.right_node)


    def handle_violation(self, node):
        # cehck the nodes from the node we have insert up to root node
        while node is not None:
            node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

            self.violation_helper(node)
            # whenever we settle a violation (rotattion) it may happen that it
            # violates the AVL properties in other part of the tree
            node = node.parent

    # checks whether the subtree is balanced with root node = node
    def violation_helper(self, node):
        balance = self.calculate_balance(node)

        # ok, we know the tree is left heavy but it can be left-right heavy or left-left heavy
        if balance > 1:
            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            
            # this is the right rotation on grandparent (if left-left heavy, that's single right rotation)
            self.rotate_right(node.left_node)

        # ok, we know the tree is right heavy BUt it can be left-right heavy or right-right heavy
        if balance < -1:
            # right - left heavy so we need a right rotation before left rotation
            if self.calcualte_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)

            self.rotate_left(node)

    def rotate_right(self, node):
        print("Rotating to the right on node", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None  and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_node),self.calc_height(node.right_node)) + 1
        temp_left_node.height = max(self.calc_height(temp_left_node.left_node),self.calc_height(temp_left_node.right_node)) + 1



    def rotate_left(self, node):
        print("Rotating to the left on node", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None  and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.left_node),self.calc_height(node.right_node)) + 1
        temp_right_node.height = max(self.calc_height(temp_right_node.left_node),self.calc_height(temp_right_node.right_node)) + 1

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    #it has O(N) linear time complexity
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)

    

avl = AVLTree()
avl.insert(5)
avl.insert(3)
avl.insert(4)





        




























