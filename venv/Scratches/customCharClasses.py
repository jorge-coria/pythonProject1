# Short-hand char classes can be too broad, define your own using square brackets
# Caret char (^) after the char class's opening bracket makes a negative char class
# Negative char class matches all chars not in the character class

import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
matchList = vowelRegex.findall('Robotics eating Lizard food. LIZARD FOOD.')
print('Vowels extracted from String: ' + str(matchList))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
matchList2 = consonantRegex.findall('Robotics eating Lizard food. LIZARD FOOD.')
print('Consonants extracted from String: ' + str(matchList2))
