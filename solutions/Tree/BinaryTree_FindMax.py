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

    def findMax(self, root):
        """TODO: Docstring for findMax.
        :returns: TODO

        """
        if root is None:
            return 0

        # return max(root.data, self.findMax(root.left), self.findMax(root.right))
        left_max = self.findMax(root.left)
        right_max = self.findMax(root.right)
        return max(root.data, left_max, right_max)


if __name__ == "__main__":
    '''
               10
            /     \
           50      30
          / \      /  \
        40   25    80  100
                     \
                      70
    '''

    btree = BinaryTree(10)
    btree.root.left = Node(50)
    btree.root.right = Node(30)
    btree.root.left.left = Node(40)
    btree.root.left.right = Node(25)
    btree.root.right.left = Node(80)
    btree.root.right.right = Node(100)
    btree.root.right.left.right = Node(70)

    _max = btree.findMax(btree.root)
    print(_max)
