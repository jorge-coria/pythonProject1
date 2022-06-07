# Using curly brackets to match a group that repeats a specific number of times
import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
print('Match Object 1: ' + mo1.group())

mo2 = haRegex.search('Ha')
mo2 == None
print('Match Object 2: ' + str(mo2))
