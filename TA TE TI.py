print('TA TE TI')
print('Proyecto: Cintia, Luciano, Ciro Farias')
def vertablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end='\n')
            else:
                print(fila[i], end='  ')

def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo = 'x'
    else:
        simbolo = 'o'
    
    if posicion == 1:
        if tablero[4][0] == ' ':
            tablero[4][0] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada'
    


tablero = [

[' ', '|', ' ', '|', ' '],

['-', '+', '-', '+', '-'],

[' ', '|', ' ', '|', ' '],

['-', '+', '-', '+', '-'],

[' ', '|', ' ', '|', ' ']

]

demotablero = [

['7', '|', '8', '|', '9'],

['-', '+', '-', '+', '-'],

['4', '|', '5', '|', '6'],

['-', '+', '-', '+', '-'],

['1', '|', '2', '|', '3']

]

jugador_1 = str(input('Ingrese nombre del jugador 1: \n'))
jugador_2 = str(input('Ingrese nombre del jugador 2: \n '))
turno_1 = True
turno = 0
print('A continuacion vera los comandos para cada posicion del tablero')
vertablero(demotablero)
print('¡Empieza!')

while turno < 9:
    if turno_1:
        print(f'{jugador_1}, elija una posicion')
    else:
        print(f'{jugador_2}, elija una posicion')
    jugada = int(input())
    
