# Regex \d+\s\w+ matches text that has 1 or more digits, followed by a whitespace char,
# Followed by 1 or more digit/letter/underscore chars

import re

xmasRegex = re.compile(r'\d+\s\w+')
matchedList = xmasRegex.findall('12 gizzards, 11 senses, 10 universes, 9 fishies, 8 microtones, 7 cyboogies, '
                  '6 wizards, 5 lizards, 4 bananas, 3 senses, 2 times, 1 work')
print(matchedList)