class CuadroC:
    def __init__(self, coords, posibilidades):
        self.coords = coords
        self.posibilidades = posibilidades
    def actualizarPos(self, num):
        self.posibilidades.remove( num )
    def recuperarPos(self, num):
        self.posibilidades.append( num )
        
class SudokuC:

    

    def __init__(self, tablero, variables, vDyn):
        self.tablero = tablero
        self.variables = variables
        self.vDyn = variables.copy()

    def crearVariables( self ):
        variables = []
        for i in range(9):
            for j in range(9):
                if self.tablero[i][j] == 0:
                    #print( (i,j) )
                    posib = self.crearPosib( (i,j) )
                    c = CuadroC( (i,j), posib)
                    variables.append( c )
        self.ordenarV( variables )
        self.variables = variables
    

    def ordenarV( self, variables ):
        for i in range( len ( variables ) ):
            for j in range( len ( variables )-i-1 ):
                #print("Buenas")
                #print( str( len( variables[j].posibilidades ) ) )
                if( len( variables[j].posibilidades ) > len( variables[j+1].posibilidades ) ):
                    variables[ j ], variables[ j+1 ] = variables[ j+1 ], variables[ j ]
    
    def crearPosib( self , actual ):
        op = list( range( 1, 10 ) )
        
        for i in range(9):
            if self.tablero[actual[0]][i] != 0:
                try:
                    op.remove( self.tablero[actual[0]][i] )
                    
                except (ValueError):
                    continue
        for i in range(9):
            if self.tablero[i][actual[1]] != 0:
                try:
                    op.remove( self.tablero[i][actual[1]] )
            
                except (ValueError):
                    continue

        f = self.ubicacion_cuadro( actual[0] )
        c = self.ubicacion_cuadro( actual[1] )

        for i in range(f*3, f*3 + 3):
            for j in range(c*3, c*3 + 3):
                if self.tablero[i][j] != 0:
                    try:
                        op.remove( self.tablero[i][j] )
                    except (ValueError):
                        continue       

        #print( op )
        #print("\n")
        return op

    def solucionar( self, pos ):
        
        if self.tableroFull():
            return True
        
            
        for p in self.variables[pos].posibilidades:
            if( self.valido( self.variables[pos].coords, p )):
                self.tablero[self.variables[pos].coords[0]][self.variables[pos].coords[1]] = p
                if self.solucionar( pos + 1):
                    return True
                self.tablero[self.variables[pos].coords[0]][self.variables[pos].coords[1]] = p
        return False

    def valido( self, coords, p):
        f = coords[0]
        c = coords[1]
        for i in range(0,9):
            if i != f and self.tablero[i][c] == p:
                return False
        for i in range(0,9):
            if i != c and self.tablero[f][i] == p:
                return False

        f = self.ubicacion_cuadro( f )
        c = self.ubicacion_cuadro( c )

        for i in range(f*3, f*3 + 3):
            for j in range(c*3, c*3 + 3):
                if (i,j) == coords:
                    continue
                else:
                    if self.tablero[i][j] == p:
                        return False


        return True



    def tableroFull(self):
        for i in range(9):
            for j in range(9):
                if self.tablero[i][j] == 0:
                    return False
        return True


    def ubicacion_cuadro( self, coord ):
        if coord < 3:
            return 0
        if coord < 6:
            return 1
        return 2
    def imprimirCuadros( self ):
        for c in self.variables:
            print( c.coords )
            print( c.posibilidades )


    