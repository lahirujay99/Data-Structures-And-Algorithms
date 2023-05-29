import math


def binary_search(arr, low, high, x):
    # check base case
    if high >= low:
        mid = math.floor((high + low) / 2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1



git remote add origin https://github.com/lahirujay99/Data-Structures-And-Algorithms.git
git branch -M main
git push -u origin main