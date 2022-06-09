# When you want to match letters without worrying about lower/upper-case, pass re.IGNORECASE to re.compile()

import re

robocop = re.compile(r'robocop', re.I)
mo1 = robocop.search('RoBoCOP is part man, part machine, all cop!')
print('Match Object 1: ' + str(mo1.group()))
