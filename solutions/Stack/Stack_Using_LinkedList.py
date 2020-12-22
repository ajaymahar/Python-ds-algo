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


class Stack:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.head = None
        self.size = 0

    def push(self, data):
        """TODO: Docstring for push.
        :returns: TODO

        """
        if self.head:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            self.size += 1
        else:
            self.head = Node(data)
            self.size += 1

    def pop(self):
        """TODO: Docstring for pop.
        :returns: TODO

        """
        if self.size == 0:
            return None
        tmpHead = self.head
        self.head = tmpHead.next
        self.size -= 1
        tmpHead.next = None
        return tmpHead.data

    def peek(self):
        """TODO: Docstring for peek.

        :arg1: TODO
        :returns: TODO

        """
        if self.head:
            return self.head.data
        return None

    def isEmpty(self):
        """TODO: Docstring for isEmpty.
        :returns: TODO

        """
        return self.size == 0


if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.push(50)

    print(st.peek())
    print(st.size)
    print(st.isEmpty())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.isEmpty())
