# using the max_number function to find max # in a user's list
def max_number(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


# number of elements
n = int(input('Enter number of elements : '))

# Read inputs from user using map() function
userList = list(map(int, input('Enter the numbers : ').strip().split()))[:n]
print(max_number(userList))
