# Iterate through string with two pointers, one on each side of string and compare the characters
# Time Complexity: O(n) | Memory: O(1)

def alpha_num(c):
    return (('a' <= c.lower() <= 'z') or ('0' <= c <= '9'))

def is_palindrome(string):
    string = string.lower()
    l, r = 0, len(string) - 1
    while l < r:
        if not alpha_num(string[l]):
            l += 1
            continue
        if not alpha_num(string[r]):
            r -= 1
            continue
        if string[l] != string[r]:
            return False
        l, r = l + 1, r - 1

    return True

q = "A man, a plan, a canal: Panama"
r = "race a car"
s = " "

print(is_palindrome(q))
print(is_palindrome(r))
print(is_palindrome(s))