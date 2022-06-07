# The (.) char in a regex is a wildcard -> matches any char except for a newline
# Actual dot escaped with backslash. \..

import re

atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print('Match Object 1: ' + str(mo1))
