import re

text = '''
Hi, today is 17-Apr-2021, yesterday was 16-Apr-2021 and tomorrow will be 18-Apr-2021.
My schedule is free on 26-04-2021, 06.05.2021 and 16/Jun/2021.
You can reach out to me at myname2020@dummy.com or ask_help@demo.net & conference@demo.co.in
You can also call me at one of the following no's +6032-007 1212, +6099.100 3344, 017-9998800 etc.
'''
# Create the pattern [] you can cutomize your pattern, ()This will create the group. 
datePattern = re.compile(r'\d{2}[-./]([a-zA-z]{3}|\d{2})[-./]\d{4}')
emailPattern = re.compile(r'\w+@[a-z]+(\.[a-z]{2,3})+')

# Search for the date pattern
matches = datePattern.finditer(text)
matches1 = emailPattern.finditer(text)

#Print
for match in matches1:
    print(match.group())