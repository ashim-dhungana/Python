import re

pattern1 = "line"

pattern2 = r"[A-Z]+eaning"

text = '''
    This is a line of text which has absolutely no fucking Meaning. This line of text is completely meaningless. Meaning and Feaning.
'''

match = re.search(pattern1,text)
print(match)
print('\n')

matches = re.finditer(pattern2,text)
for match in matches:
    print(match)