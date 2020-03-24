flag = True
while flag:
    val_1 = int(input('Input first number: '))
    val_2 = int(input('Input second number: '))
    command = input('input operation: ')
    if command == '+':
        print(val_1 + val_2)
    elif command == '-':
        print(val_1 - val_2)
    elif command == '*':
        print(val_1 * val_2)
    elif command == '/':
        print(val_1 / val_2)
    else:
        print('Wrong command')
    for i in range(3):
        command = input('Continue?(Y/N)')
        if command == 'Y':
            break
        elif command == "N":
            flag = False
            break
        else:
            print('Wrong command')
        if i == 2:
            print('Too much errors')
            flag = False
            break



