'''
    Author: Ajay Mahar
    Lang: python3
    Github: www.github.com/ajaymahar
    YT: www.youtube.com/ajaymahar

'''


class Node:
    def __init__(self, data):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.root = Node(data)

    def preOrder(self, root):
        """TODO: Docstring for preOrder.
            root->left->right
        :returns: TODO

        """
        if root is None:
            return

        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        """TODO: Docstring for inOrder.
           left->root->righ
        :returns: TODO

        """
        if root is None:
            return

        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def postOrder(self, root):
        """TODO: Docstring for postOrder.
            left->right->root
        :returns: TODO

        """
        if root is None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")


if __name__ == "__main__":
    '''
               10
            /     \
           20      30
          / \      / \
        40   50    60 70
    '''

    btree = BinaryTree(10)
    btree.root.left = Node(20)
    btree.root.right = Node(30)
    btree.root.left.left = Node(40)
    btree.root.left.right = Node(50)
    btree.root.right.left = Node(60)
    btree.root.right.right = Node(70)

    btree.preOrder(btree.root)
    print("\n")
    btree.inOrder(btree.root)
    print("\n")
    btree.postOrder(btree.root)
