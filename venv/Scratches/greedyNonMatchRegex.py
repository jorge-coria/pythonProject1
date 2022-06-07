# Using (?) after curly brackets to return the shortest string possible ; Python greedy by default
# (?) -> Two meanings in regular expressions: flag optional group or declare a nongreedy match
import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
print('Match Object 1: ' + mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo1.group()
print('Match Object 2: ' + mo2.group())
