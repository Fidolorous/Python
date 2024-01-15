while True :
    line = input('enter a number ')
    if line == 'Done':
        break
    print(line)
print

try:
    x = int(line)
    c = len(x)
    print(c)
except:
    print('Please enter a number')
    