import re
import requests

BASE_URL = 'http://162.105.138.126/OnLineReader/command/imagepage.ashx?......'

PATTERN = re.compile(r'(?<=&pageid=)\d+(?=&)')

i = 1
while True:
    r = requests.get(PATTERN.sub(str(i), BASE_URL))
    if r.ok and len(r.content) > 0:
        with open("%03d.png" % i, "wb") as f:
            f.write(r.content)
        print(i)
        i += 1
    else:
        break
