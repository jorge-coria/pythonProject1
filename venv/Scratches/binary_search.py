def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [5,3,3,4,6,7]
x = 'Index is:'
print(x, binary_search(my_list, 3))
print(x, binary_search(my_list, -1))