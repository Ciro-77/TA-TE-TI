print('TA TE TI')
print('Proyecto: Cintia, Luciano, Ciro Farias')
def vertablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end='\n')
            else:
                print(fila[i], end='  ')


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
        print(f'{jugador_1}Elija una posicion')

    
