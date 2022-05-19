# recursive to count number of items in a list
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

userList = [5,4,3,2,1,0]
print(count(userList))