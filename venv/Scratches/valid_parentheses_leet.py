# Iterate string, add char to stack and pop if matching char is in hashmap
# Time + Memory Complexity: O(n)

def isValid(string):
    stack = []
    hashMap = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for c in string:
        if c in hashMap:
            if stack and stack[-1] == hashMap[c]:
                stack.pop()
        else:
            stack.append(c)

    return True if not stack else False


print(isValid(')('))        # False
print(isValid('()'))        # True
print(isValid('({})'))      # True
print(isValid('({[]})'))    # True
