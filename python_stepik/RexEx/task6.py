
import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'human','computer', line))
