import re
def required():
    a = input('''
    please select one choice:
   +
   _
   *
   /
    ''')
    if not re.match("^[+,-,/]",a):
        print("please input above")
        required()
required