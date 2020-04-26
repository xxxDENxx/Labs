flag = True
while flag:
    data1 = []
    dict1 = {}
    print('There are your parameters:')
    with open ('conf','r') as data:
        for line in data:
            if line[0] != '#' and line[0] != '\n' and line[0] != ';':
                pack = line.strip().split(' ', 1)
                value = None
                if len(pack) == 1:
                    pack.append(value)
                dict1[pack[0]] = pack[1]
                print(pack[0])
    key = input('Enter the required parameter:\nget param ')
    if key in dict1:
        print('Your parameter: ', key,'\nIts value:\t', dict1[key])
    else:
        print("This file does not have this parameter.")
    for i in range(3):
        command = input("Repeat?(Y/N) ").upper()
        if command == 'Y':
            break
        elif command =='N':
            flag = False
            break
        else:
            print("Wrong command")
        if i == 2:
            print("Too many mistakes. Goodbye")
            flag = False