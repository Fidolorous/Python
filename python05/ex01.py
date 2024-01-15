Gehy = None
print('Before:', Gehy)
for line in input('enter a number '):
    if Gehy is None or input > Gehy :
        Gehy = input
        if line == 'Done':
            break
    print(line)
x = len(line)
print(x)


""" try:
    x = int(line)
    c = len(x)
    print(c)
except:
    print('Please enter a number')
     """