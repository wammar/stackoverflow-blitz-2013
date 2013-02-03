import sys
import json
from pprint import pprint

filename = sys.argv[-1]

f1 = open(filename, 'r')

for line in f1:
  obj = json.loads(line)
  pprint(obj)

f1.close()
