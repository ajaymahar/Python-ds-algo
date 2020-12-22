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
        self.next = None


class Queue:
    def __init__(self):
        """TODO: Docstring for __init__.

        :arg1: TODO
        :returns: TODO

        """
        self.front = None
        self.rare = None
        self.size = 0

    def enque(self, data):
        """TODO: Docstring for enqueue.
        :returns: TODO

        """
        newNode = Node(data)
        if self.rare:
            self.rare.next = newNode
            self.rare = newNode
        else:
            self.rare = newNode
            self.front = newNode
        self.size += 1

    def deque(self):
        """TODO: Docstring for deque.

        :arg1: TODO
        :returns: TODO

        """
        if not self.front:
            return None

        tmpFront = self.front
        self.front = tmpFront.next
        tmpFront.next = None
        self.size -= 1
        return tmpFront.data

    def isEmpty(self):
        """TODO: Docstring for isEmpty.
        :returns: TODO

        """
        return self.getSize() == 0

    def getSize(self):
        """TODO: Docstring for size.
        :returns: TODO

        """
        return self.size


if __name__ == "__main__":
    q = Queue()
    q.enque(10)
    q.enque(20)
    q.enque(30)
    q.enque(40)
    q.enque(50)
    q.enque(60)

    print(q.isEmpty())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.isEmpty())
