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

    def insertionSort(self, arr):
        """TODO: Docstring for insertionSort.
        :returns: TODO

        T: O(n^2)
        S: O(1)
        """
        for i in range(1, len(arr)):
            tmp = arr[i]
            j = i - 1

            while (j >= 0 and arr[j] > tmp):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1

            arr[j + 1] = tmp


if __name__ == "__main__":
    sort = Sort()
    arr = [2, 4, 21, 5, 76, 4, 2, 7, 8, 4, 2, 7, 89, 34]

    sort.insertionSort(arr)
    print(arr)
