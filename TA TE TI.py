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

jugador_1 = str(input('Ingrese nombre del jugador 1: \n'))
jugador_2 = str(input('Ingrese nombre del jugador 2: \n '))
turno_1 = True
turno = 0

