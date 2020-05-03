sudoku = [
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
    f = cuadroAct[0] // 3
    c = cuadroAct[1] // 3
    for i in range(f*3, f*3 + 3):
        for j in range(c*3, c*3 + 3):
            if (i,j) == cuadroAct:
                continue
            else:
                if sudoku[i][j] == nNuevo:
                    return False


    return True


def respuesta( sudoku, fileR ):
    cuadro = selec_cuadro( sudoku )
    if cuadro == -1:
        return True
    else:
        f = cuadro[0]
        c = cuadro[1]

    #print( f, c )
    for i in range(1,10):
        if validar(sudoku, i, (f,c)):
            sudoku[f][c] = i
            imprimir2(sudoku, fileR)

            if respuesta( sudoku, fileR ):
                return True

            sudoku[f][c] = 0

    return False

def leer_sudoku1():
    sud = []
    fila = []
    print( "Ingrese 0 para los espacios en blanco" )
    for i in range(9):
        fila.clear()
        for j in range(9):
            n = int( input("Ingrese el valor de la cuadro fila: " + str(i) + " columna: " + str(j) + "\n"))
            fila.append(n)
        sud.append( fila )
    return sud

def leer_sudoku2( fname ):
    arch = open( fname, "r")
    sud = []
    fil = []
    for i in range(9):
        fila = arch.readline()
        nums = fila.split(" ")
        for j in range(9):
            fil.append( int(nums[j]) )

        sud.append( fil )
    arch.close()
    return sud

name = input("Ingrese el nombre del archivo del proceso: ")
#sudoku = []
#op = ""
#while op != "1" and op != "2":
#    op = input("1. Ingresar tablero a mano\n2. Ingresar por archivo\n")
#
#if op == "1":
#    sudoku = leer_sudoku1()
#else:
#    fname = input("Ingrese el nombre del archivo del sudoku: ")
#    sudoku = leer_sudoku2(fname)

f = open(  name ,"w" )
imprimir( sudoku )
imprimir2( sudoku, f )
respuesta( sudoku, f )
print( "\n\n\n\nSolución del sudoku:")
imprimir( sudoku )
f.close()
