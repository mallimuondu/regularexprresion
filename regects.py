def empty():
    a = input('''
    1.Malli
    2.Nesh
    3.Manna
    ''')
    if a == "":
        print("please enter input")
        empty()
    else:
        print(a)
empty()