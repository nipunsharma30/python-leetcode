a ={'a': 2, 'b': 33, 'c': 1, 'f': 4, 'e': 1}
a
sorted(a)

for i in a:
    print(a[i])
    if 'z' in a.keys():
        print(True)