BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range (6):
    if i < 2:
        print(f'{BLACK}{"  " * (3)}{WHITE}{"  " * (3)}{BLACK}{"  " * (3)}{END}')
    elif i > 1 and i < 4:
        print(f'{WHITE}{"  " * (3)}{BLACK}{"  " * (3)}{WHITE}{"  " * (3)}{END}')
    else:
        print(f'{BLACK}{"  " * (3)}{WHITE}{"  " * (3)}{BLACK}{"  " * (3)}{END}')
