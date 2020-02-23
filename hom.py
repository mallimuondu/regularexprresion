import re
def malli():
    a = input('''
    please select one choice:
   $
   %
    ''')
    if not re.match("^[$,%]",a):
        print("please input one above")
        malli()
malli()