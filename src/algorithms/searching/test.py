import search_methods

arr = [4, 6, 9, 13, 14, 18, 21, 24, 38]
x = 13
result = search_methods.binary_search(arr, 0, len(arr) - 1, x)
print(result)
