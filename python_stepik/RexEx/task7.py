# put your python code here
# put your python code here

import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'\b[aA]+\b', r'argh', line, 1))
