import re

# search() returns Match object of first matched text
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print('Match Object 1: ' + mo.group())

# findall() returns a list of strings as long as there are no groups in the Regex; will not return a Match object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # no groups
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print('Match Object 2: ' + str(mo2))

# findall() returns a list of tuples, each tuple's items are matched strings for each group in Regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo3 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print('Match Object 3: ' + str(mo3))