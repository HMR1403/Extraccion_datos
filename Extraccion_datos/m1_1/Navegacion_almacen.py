#Hector Malaga Rodriguez, 951, 21 de Agosto del 2026
#Ejercicio 3. El robot que camina por el almacen, buen juego
el_almacen = [['.','.','#','P'],
              ['.','#','.','.'],
              ['P','.','P','.'],
              ['#','.','#','.']
              ]


def verificar_recorrido(almacen, movimientos):
    total_productos = 0
    for fila in almacen:
        total_productos += fila.count('P')

    fila = 0
    columna = 0
    producto_recogidos = 0

    for movimiento in movimientos:
        if movimiento == 'R':
            columna += 1
        elif movimiento == 'D':
            fila += 1
        elif movimiento == 'L':
            columna -= 1
        elif movimiento == 'U':
            fila -= 1
        else:
            return False

        if fila < 0 or fila > len(almacen):
            return False

        if columna < 0 or columna > len(almacen[0]):
            return False

        if almacen[fila][columna] == '#':
            return False

        if almacen[fila][columna] == 'P':
            producto_recogidos += 1
            almacen[fila][columna] = '.'

    if producto_recogidos == total_productos and fila == 0 and columna == 0:
        return True
    else:
        return False

movimientos_correctos = ['D','D','R','R','U','R','U','D','D','L','L','L','U','U']
print(verificar_recorrido(el_almacen, movimientos_correctos))
# True
