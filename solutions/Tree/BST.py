'''
    Author: Ajay Mahar
    Lang: python3
    Github: https://www.github.com/ajaymahar
    YT: https://www.youtube.com/ajaymaharyt

'''


class Node:
    def __init__(self, data):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.root = None

    # recursive method to insert node in a BST
    def insert(self, root, key):
        """TODO: Docstring for insert.
        :returns: TODO

        """
        if root is None:
            return Node(key)

        if root.data == key:
            return root
        elif root.data > key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    # iterative method to insert node in BST
    def Iinsert(self, root, key):
        """TODO: Docstring for Iinsert.

        :key: TODO
        :returns: TODO

        """
        if root is None:
            return Node(key)

        prev = None
        curr = root

        while curr:
            prev = curr
            if root.data == key:
                return root
            elif root.data > key:
                curr = curr.left
            else:
                curr = curr.right
        newNode = Node(key)
        if prev.data > key:
            prev.left = newNode
        else:
            prev.right = newNode

        return root

    def search(self, root, key):
        """TODO: Docstring for search.
        :returns: TODO

        """
        if root is None:
            return None

        curr = root
        while curr:
            if curr.data == key:
                return True
            elif curr.data > key:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def inOrder(self, root):
        """TODO: Docstring for inOrder.
        :returns: TODO

        """
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)


if __name__ == "__main__":
    '''
             9
           /  \
          5    15
         / \   / \
        3   8  12 20
            /    /
           6    16

    '''
    bst = BST()

    # create BST using Recursive method
    root = bst.insert(bst.root, 9)
    bst.insert(root, 15)
    bst.insert(root, 5)
    bst.insert(root, 20)
    bst.insert(root, 16)
    bst.insert(root, 8)
    bst.insert(root, 12)
    bst.insert(root, 3)
    bst.insert(root, 6)

    # create BST using Iterative method
    # root = bst.Iinsert(bst.root, 9)
    # bst.Iinsert(root, 15)
    # bst.Iinsert(root, 5)
    # bst.Iinsert(root, 20)
    # bst.Iinsert(root, 16)
    # bst.Iinsert(root, 8)
    # bst.Iinsert(root, 12)
    # bst.Iinsert(root, 3)
    # bst.Iinsert(root, 6)

    # print inOrder traversal to check
    # BST is correct, if inorder is printing
    # data in sorted order that means your BST is right
    bst.inOrder(root)
    isExist = bst.search(root, 12)
    print(isExist)
