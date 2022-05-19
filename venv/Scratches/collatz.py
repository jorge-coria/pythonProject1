import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

print()
print('Type an integer:')
try:
        userInt = int(input())

        result = collatz(userInt)
        while result != 1:
            result = collatz(result)
        if result == 1:
            sys.exit()
except ValueError:
    print('Please enter a number of integer type')