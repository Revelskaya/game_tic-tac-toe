#тест на корректность введенных X и Y
def check(a, x, y):
    if x > 2 or y > 2 or a[x][y] != 0:
        print('введите другие X и Y')
    else:
        a[x][y] = 1

    
#тест на победу одного из участников
def winCheck(a):
    for line in a:
        if not (1 in line) and not (0 in line):
            print('бот победил')
        if not (2 in line) and not (0 in line):
            print('игрок победил')

    if not 2 in (a[0][0], a[1][1], a[2][2]) and not 0 in (a[0][0], a[1][1], a[2][2]):
        print('Игрок победил')
    elif not 1 in (a[0][0], a[1][1], a[2][2]) and not 0 in (a[0][0], a[1][1], a[2][2]):
        print('Бот победил')
    elif not 2 in (a[0][2], a[1][1], a[2][0]) and not 0 in (a[0][2], a[1][1], a[2][0]):
        print('Игрок победил')
    elif not 1 in (a[0][2], a[1][1], a[2][0]) and not 0 in (a[2][0], a[1][1], a[2][0]):
        print('Бот победил')
    
    for i in range(3):  
        if not (1 in (a[0][i], a[1][i], a[2][i])) and not (0 in (a[0][i], a[1][i], a[2][i])):
            print('Бот победил')
            break
        if not 2 in (a[0][i], a[1][i], a[2][i]) and not 0 in (a[0][i], a[1][i], a[2][i]):
            print('Игрок победил')
            break
    
