# Use sub() to replace any matches in a string of text

import re

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('CENSORED','Agent Allison gave the secret documents to Agent Billy.')
print('Match Object 1: ' + str(mo1))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo2 = agentNamesRegex.sub(r'\1****', 'Agent Allison told Agent Carol that Agent Eva knew Agent Bibby'
                                     ' was a double agent.')
print('Match Object 2: ' + str(mo2))
