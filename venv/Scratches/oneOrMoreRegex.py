# Group that precedes the (+) must appear at least once
import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
print('Match Object 1: ' + mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
print('Match Object 2: ' + mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
print('Match Object 3: ' + str(mo3))
