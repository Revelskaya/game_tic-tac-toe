a = [[0,0,0],[0,0,0],[0,0,0]]
if x > 2 or y > 2 or a[x][y] != 0:
    print('введите другие X и Y')
else:
    a[x][y] = 1

for line in a:
    if not (1 in line) and not (0 in line):
        print('бот победил')
    if not (2 in line) and not (0 in line):
        print('игрок победилы')
