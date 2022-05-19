def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


"""
Getting a list of numbers as input from user
Using List Comprehension and Typecasting
This way we don't have to ask user for a number of elements, like we do with map()
Instead, user enters the list of numbers right away
"""
userInput = [int(item) for item in input('Enter the numbers to be sorted, separated by a space : ').split()]

print(selectionSort(userInput))
