
spam = ['apples', 'bananas', 'tofu', 'cats']


def commaSpace(list):
    for x in range(len(list)):
        if x == len(list) - 1:
            print('and ' + list[len(list) - 1])
        else:
            print(list[x] + ', ')


commaSpace(spam)

# First solution all by myself haha :p