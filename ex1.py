import re
import requests
import os

raw = open('files/Hello.txt' , 'r')
content = raw.read()

SearchRegex = re.compile(r'\w\w\w\w\w\w')
mo = SearchRegex.findall(content)
print(mo)