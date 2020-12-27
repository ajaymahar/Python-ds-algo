'''
    Author: Ajay Mahar
    Lang: python3
    Github: https://www.github.com/ajaymahar
    YT: https://www.youtube.com/ajaymaharyt

'''


class Sort:
    def __init__(self):
        """TODO: Docstring for __init.
        :returns: TODO

        """
        pass

    def merge(self, arr, low, mid, high):
        """TODO: Docstring for merge.
        :arr, low, mid, high: TODO
        :returns: TODO

        """
        leftArray = arr[low:mid + 1]
        rightArray = arr[mid + 1:high + 1]

        i = j = 0
        k = low

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
                k += 1
            else:
                arr[k] = rightArray[j]
                j += 1
                k += 1
        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1
        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1

    def mergeSort(self, arr, low, high):
        """TODO: Docstring for mergeSort.
        : arr, low, high: TODO
        :returns: TODO

        T: O(n log n)
        S: O(n)

        """
        if low < high:
            mid = low + (high - low)//2

            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)

            self.merge(arr, low, mid, high)


if __name__ == "__main__":
    ms = Sort()

    test_arrs = [
        [10, 3, 5, 9, 8, 3, 43, 23, 9, 1, 54],
        [],
        [7],
        [7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]

    ms.mergeSort([4, 3, 2, 1, 5, 6, 7, 8], 0, 7)
    for arr in test_arrs:
        ms.mergeSort(arr, 0, len(arr) - 1)
        print(arr)
