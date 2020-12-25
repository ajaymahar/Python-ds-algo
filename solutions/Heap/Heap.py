'''
    Author: Ajay Mahar
    Lang: python3
    Github: https://www.github.com/ajaymahar
    YT: https://www.youtube.com/ajaymaharyt

'''


class Heap:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """

    def insertHeap(self, arr, index):
        """TODO: Docstring for insert.
        :returns: TODO
        1. if index is not 0 and newly added item is > it's parent
        2. then swap the element with it's parent
        3. move index at the place where newly added element is swaped

        NOTE: To get the parent of node use the formula (index -1) // 2
        parent = (index -1)//2
        leftnode = index * 2 + 1
        rightnode = index * 2 + 2

        Time taken by inserting 1 element to heap is (log n)
        so, for n element time would be

        T: O(n log n)
        S: O(1) -> bcz we are doing swapping in place, no additional array used to sort.

        """
        while index > 0 and arr[index] > arr[(index - 1)//2]:
            arr[index], arr[(index - 1)//2] = arr[(index - 1)//2], arr[index]
            index = (index - 1)//2

    def heapify(self, arr, n):
        """TODO: Docstring for heapify.
        :returns: TODO

        heapify function takes less time to create max heap as compared
        to insert function.
        we do very less adjustment.

        heapify depends on the hight of a tree 'h', which is equal to
        O(n), where n is number of nodes.

        hight increases as we move upwords along the tree

        T: O(n)
        S: O(1) -> bcz we are doing swapping in place, no additional array used to sort.

        """
        for i in range(n//2 - 1, -1, -1):
            # j will point to i'th left child
            j = (2 * i) + 1

            # push lower value down till j is  < len(arr) -1
            while j < n-1:
                # if right node is > left node, then j will point to gragter item
                if arr[j+1] > arr[j]:
                    j = j+1
                # check if parent node is less than the grater item
                if arr[i] < arr[j]:
                    # swap the value, (push small value down words)
                    arr[i], arr[j] = arr[j], arr[i]
                    i = j
                    j = (2 * i) + 1
                else:
                    break

    def deleteHeap(self, arr, index):
        """TODO: Docstring for deleteHeap.
        :returns: TODO
        Steps:
        1. initialize i to root node which needs to be deleted
        2. swap root value with  last element of an array
        3. move j  to it's left child  using (i*2) + 1
        4. loop through till elements are not sorted arr
        5. check which child is grater lchild or rchild, which is grater move j to point grater child
        6. compare is newly swaped node value is less than, where j is pointing
        7. swap the value and move i into j'th position and move j into next child
        8. if root value is grater than it's lchild and rchild then break the loop.

        Delete the root node will take constant time, which is O(1)
        but after deletion we need to re-arange the max tree for that we have to
        adjust the tree which will take (log n) time.

        so, to delete n element from the tree, would take
        T: O(n log n)
        S: O(1) -> bcz we are doing swapping in place, no additional array used to sort.
        """
        i = 0
        j = (i * 2) + 1

        if arr[0] > arr[index]:
            arr[0], arr[index] = arr[index], arr[0]

        while j < index - 1:
            if arr[j + 1] > arr[j]:
                j = j+1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
                j = (i * 2) + 1
            else:
                break


if __name__ == "__main__":
    heap = Heap()
    # arr = [30, 20, 10, 40, 15, 12, 25]
    # arr = [10, 20, 30, 25, 5, 40, 35]
    arr = [33, 35, 42, 10, 7, 8, 14, 19, 48]

    # create max heap by inserting element one by one
    # for index in range(1, len(arr)):
    #     heap.insertHeap(arr, index)

    # create max heap using heapify
    heap.heapify(arr, len(arr))

    # delete max value and store them into last position of an array
    # in first itreation pass the hole array
    # once the first element is sorted pass the  len(arr) -1
    # then len(arr) -2 and so on...
    # so here we are passing an array in reverse order
    for index in range(len(arr) - 1, 0, -1):
        heap.deleteHeap(arr, index)

    for item in arr:
        print(item, end=" ")
