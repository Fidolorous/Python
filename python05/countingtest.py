count = 0
total = 0
while True:
        user_input = input('Enter a number')
        if user_input == 'done':
            break
        count = count + 1
        total = total + float(value)
        print(user_input)
print('Results are:', count, total, total / count)