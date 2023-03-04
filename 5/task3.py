#Создайте программу для игры в ""Крестики-нолики"".
field = [ ['1','2','3'], ['4','5','6'],['7','8','9']]

def ShowField():
    print(field[0])
    print(field[1])
    print(field[2])

def isWin(f, symvol):
    result =  (f[0][0],f[0][1],field[0][2]) == (symvol, symvol, symvol)
    result =  (f[1][0],f[1][1],field[1][2]) == (symvol, symvol, symvol) or result        
    result =  (f[2][0],f[2][1],field[2][2]) == (symvol, symvol, symvol) or result        
    result =  (f[0][0],f[1][0],field[2][0]) == (symvol, symvol, symvol) or result        
    result =  (f[0][1],f[1][1],field[2][1]) == (symvol, symvol, symvol) or result        
    result =  (f[0][2],f[1][2],field[2][2]) == (symvol, symvol, symvol) or result        
    result =  (f[0][0],f[1][1],field[2][2]) == (symvol, symvol, symvol) or result        
    result =  (f[2][0],f[1][1],field[0][2]) == (symvol, symvol, symvol) or result        
    return result

def isPat(f):
    result = True
    for i in range(3):
        for j in range(3):
            result = result and f[i][j] in {'O','X'}
    return result

def isFree(f, digit, symvol):
    row = (digit - 1) // 3
    column = (digit - 1) % 3
    if row > 2 or column > 2:
        return False
    free = not f[row][column] in {'O','X'}
    if free:
        f[row][column] = symvol
        return True
    return False

currentPlayer = 0
players = [False, False]
step = 0
while not players[0] and not players[1] and step < 9:
    print()
    ShowField()  
    step += 1
    position = 0  
    free = False
    symvol = 'X'
    if currentPlayer == 0:
        symvol = 'O'
    while not free and not players[0] and not players[1] and not isPat(field):
        position = int(input(f'{currentPlayer + 1}-й Сделайте правильный ход в незанятую позицию: '))
        free = isFree(field, position, symvol)
        players[0] = isWin(field, 'O') 
        players[1] = isWin(field, 'X') 
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0
print()
if players[0]:
    print('Победил 1й игрок')        
elif players[1]:
    print('Победил 2й игрок')        
else:
    print('НИЧЬЯ!')            
print()
ShowField()                 
