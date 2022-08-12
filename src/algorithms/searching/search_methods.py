def binary_search(arr, start, end, key):

    while start <= end:
        mid = int(start + (end - start) / 2)

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1
