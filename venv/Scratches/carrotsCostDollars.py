# Carrots cost dollars -> Caret comes first and Dollar-sign comes last in Regex

import re

# (^) used at start of a regex indicates a match must occur at the beginning of searched text
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print('Match object 1: ' + mo1.group())

mo2 = beginsWithHello.search('He said hello.') == None
print('No match for mo2? : ' + str(mo2))

# ($) used at end of a regex indicates a match must occur at the end of searched text
endsWithNumber = re.compile(r'\d$')
mo3 = endsWithNumber.search('Your number is 42')
print('Match object 3: ' + mo3.group())

mo4 = beginsWithHello.search('Your number is forty two.') == None
print('No match for mo4? : ' + str(mo4))

# r'^\d+$' matches strings that both begin and end with one or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
mo5 = wholeStringIsNum.search('1234567890')
print('Match object 5: ' + mo5.group())

mo6 = wholeStringIsNum.search('12345xyz67890') == None
print('No match for mo6? : ' + str(mo6))

mo7 = wholeStringIsNum.search('12 34567890') == None
print('No match for mo7? : ' + str(mo7))
