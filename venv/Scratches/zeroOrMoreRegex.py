# Group that precedes the asterisk can occur any number of times in the text
import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
print('Match Object 1: ' + mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
print('Match Object 2: ' + mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
print('Match Object 3: ' + mo3.group())
