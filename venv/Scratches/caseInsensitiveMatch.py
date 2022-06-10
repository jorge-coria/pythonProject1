# When you want to match letters without worrying about lower/upper-case, pass re.IGNORECASE to re.compile()

import re

robocop = re.compile(r'robocop', re.I)
mo1 = robocop.search('RoBoCOP is part man, part machine, all cop!')
print('Match Object 1: ' + str(mo1.group()))

mo2 = robocop.search('ROBOCOP is part man, part machine, all cop!')
print('Match Object 2: ' + str(mo2.group()))

mo3 = robocop.search('roboCOP is part man, part machine, all cop!')
print('Match Object 3: ' + str(mo3.group()))
