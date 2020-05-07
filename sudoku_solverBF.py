def imprimir( sudoku ):

    for i in range(len( sudoku )):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range( len( sudoku[0] ) ):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print( sudoku[i][j] )
            else:
                print( str( sudoku[i][j] ) + " ", end="")


def imprimir2( sudoku, fileR ):
    fileR.write("\n\n")
    for i in range(len( sudoku )):
        if i % 3 == 0 and i != 0:
            fileR.write("- - - - - - - - - - - - - \n")

        for j in range( len( sudoku[0] ) ):
            if j % 3 == 0 and j != 0:
                fileR.write(" | ")

            if j == 8:
                fileR.write( str( sudoku[i][j] ) )
            else:
                s = str( sudoku[i][j] ) + " "
                fileR.write( s )
        fileR.write("\n")


def lanzar_dados():
    a = rand(0,9)
    b = rand(0,9)
    return (a,b)

def selec_cuadro( sudoku ):

    t = len( sudoku )
    for i in range( t ):
        for j in range( t ):
            #print( t )
            if sudoku[i][j] == 0:
                #print( i,j )
                return (i,j)

    #while 1:
    #    cuadro = lanzar_dados()
    #    if sudoku[cuadro[0]][cuadro[1]] == 0:
    #        break
    return -1
def validar(sudoku, nNuevo, cuadroAct):
    # Pillar columna
    for i in range(0,9):
        if i != cuadroAct[0] and sudoku[i][cuadroAct[1]] == nNuevo:
            return False

    # Pillar fila

    for i in range(0,9):
        if i != cuadroAct[1] and sudoku[cuadroAct[0]][i] == nNuevo:
            return False

    # Pillar cuadro
    #f = cuadroAct[0]
    #c = cuadroAct[1]
    #for i in range(f-1, f+2):
    #    for j in range(c-1, c+2):
    #        if (i,j) == cuadroAct:
    #            continue
    #        else:
    #            if sudoku[i][j] == nNuevo:
    #                return False

    #Esto saca cuál cuadro 3x3 corresponde al cuadro
    f = ubicacion_cuadro( cuadroAct[0] )
    c = ubicacion_cuadro( cuadroAct[1] )

    for i in range(f*3, f*3 + 3):
        for j in range(c*3, c*3 + 3):
            if (i,j) == cuadroAct:
                continue
            else:
                if sudoku[i][j] == nNuevo:
                    return False


    return True

def ubicacion_cuadro( coord ):
    if coord < 3:
        return 0
    if coord < 6:
        return 1
    return 2

def respuesta( sudoku ):
    cuadro = selec_cuadro( sudoku )
    if cuadro == -1:
        return True
    else:
        f = cuadro[0]
        c = cuadro[1]

    #print( f, c )
    #Hace practicamente lo mismo que sacar las posibles opciones de esa casilla
    for i in range(1,10):
        if validar(sudoku, i, (f,c)):
            sudoku[f][c] = i
            #imprimir2(sudoku, fileR)

            if respuesta( sudoku ):
                return True

            sudoku[f][c] = 0

    return False

def seleccionar_opciones():

    sudoku1 = [
        [9,0,1,3,0,8,7,5,0],
        [0,0,3,0,0,0,0,1,6],
        [5,0,2,1,0,6,9,3,0],
        [4,3,0,0,9,0,0,7,0],
        [1,0,0,0,4,7,0,0,5],
        [0,2,0,8,0,3,6,4,9],
        [2,0,4,0,0,1,0,8,2],
        [0,0,0,9,8,0,0,0,2],
        [6,0,0,0,3,5,0,0,0]
    ]

    sudoku2 = [
        [9,0,1,3,0,8,7,5,0],
        [0,0,3,0,0,0,0,1,6],
        [5,0,2,1,0,6,9,3,0],
        [4,3,0,0,9,0,0,7,0],
        [1,0,0,0,4,7,0,0,5],
        [0,2,0,8,0,3,6,4,9],
        [2,0,4,0,0,1,0,8,2],
        [0,0,0,9,8,0,0,0,2],
        [6,0,0,0,3,5,0,0,0]
    ]
    return sudoku1

sudoku = seleccionar_opciones()
imprimir( sudoku )
#imprimir2( sudoku, f )
respuesta( sudoku )
print( "\n\n\n\nSolución del sudoku:")
imprimir( sudoku )

