'''
    Author: Ajay Mahar
    Lang: python3
    Github: https://www.github.com/ajaymahar
    YT: https://www.youtube.com/ajaymaharyt

'''


class Sort:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self.flag = True

    def bubbleSort(self, arr):
        """TODO: Docstring for bubbleSort.
        :returns: TODO

        T: O(n^2)
        S: O(1)
        """
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.flag = False
            if self.flag:
                return


if __name__ == "__main__":
    bubble = Sort()
    arr = [2, 4, 21, 5, 76, 4, 2, 7, 8, 4, 2, 7, 89, 34]

    bubble.bubbleSort(arr)
    print(arr)
