# The (.) char in a regex is a wildcard -> matches any char except for a newline
# Actual dot escaped with backslash. \..

import re

atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print('Match Object 1: ' + str(mo1))

# The (.*) chars in a regex match any char and are greedy -> They will match as much text as possible by default
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo2 = nameRegex.search('First Name: Jay Last Name: Cee')
print('Match Object 2 Group 1: ' + mo2.group(1))
print('Match Object 2 Group 2: ' + mo2.group(2))

# Use (.*?) chars to match in a non-greedy way
nongreedyRegex = re.compile(r'<.*?>')
mo3 = nongreedyRegex.search('<To serve man> for dinner.')
print('Match Object 3: ' + mo3.group())

greedyRegex = re.compile(r'<.*>')
mo4 = greedyRegex.search('<To serve man> for dinner.>')
print('Match Object 4: ' + mo4.group())

# Pass .DOTALL as a 2nd argument to re.compile() to make (.*) match all chars, including a newline character
noNewlineRegex = re.compile('.*')
mo5 = noNewlineRegex.search('Serve the common humanity.\nProtect all humans.\nFollow the law.')
print('Match object 5: ' + mo5.group())

newlineRegex = re.compile('.*', re.DOTALL)
mo6 = newlineRegex.search('Serve the common humanity.\nProtect all humans.\nFollow the law.')
print('Match object 6: ' + mo6.group())
