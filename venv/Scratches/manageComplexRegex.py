# Complicated text patterns may require long convoluted regex
# Use 'verbose mode' to ignore whitespace and commments inside of regex string

import re

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    \d{3}                             # first 3 digits
    (\s|-|\.)                         # separator
    \d{4}                             # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?      # extension
)''', re.VERBOSE)

# If you want a regex that's case insensitive and includes newlines to match DOT char, form compile() like this:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

# All three options:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
