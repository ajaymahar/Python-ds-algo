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
        pass

    def partition(self, arr, start, end):
        """TODO: Docstring for partition.

        :arr, start, end: TODO
        :returns: TODO

        """
        pivot = arr[end]
        pIndex = start

        for i in range(start, end):
            if arr[i] <= pivot:
                arr[pIndex], arr[i] = arr[i], arr[pIndex]
                pIndex += 1

        arr[end], arr[pIndex] = arr[pIndex], arr[end]

        return pIndex

    def quickSort(self, arr, start, end):
        """
        : arr, start, end: TODO
        :returns: TODO

        Avg T: O(n log n)
        Worst T: O(n^2)
        S: O(1) -> in place
        """
        if start < end:
            pIndex = self.partition(arr, start, end)
            self.quickSort(arr, start, pIndex - 1)
            self.quickSort(arr, pIndex + 1, end)


if __name__ == "__main__":
    qs = Sort()

    arr = [3, 4, 6, 7, 8, 4, 5, 3, 6, 7, 9, 0, 2, 1, 3, 4, 5,
           34, 234, 5, 2, 54, 34, 375, 3452, 46, 75, 35, 24, 30]

    qs.quickSort(arr, 0, len(arr) - 1)
    print(arr)
