def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

userList = [3,4,4]
print(sum(userList))
