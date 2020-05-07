from sudokuC import *
from tableros import *
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

imprimir( sudoku3 )
s = SudokuC(sudoku1, list(), list())
s.crearVariables()
#s.imprimirCuadros()
if( s.solucionar(0) ):
    print("\n\n\nSolución:")
    imprimir( s.tablero )
else:
    print("Fallamos")
