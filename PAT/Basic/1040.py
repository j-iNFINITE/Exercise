# -*- coding: utf-8 -*-
import re
pat=re.compile(r'.*?P.*?A.*?T.*?')
a=re.findall(pat,'APPAPT')

print(a)