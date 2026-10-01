def shaker_sort(vec):

    # inicializa origen [iz ... de]
    iz = 1
    de = k = len(vec) - 1
    print(f"Initial_,[_<->_],{vec}" )
    print(f"Range [{iz=},{de=}]" )
    while iz <= de:
        # movimiento derecha-izquierda
        for j in range(de, iz-1, -1):
            if vec[j-1] > vec[j]:
                vec[j-1], vec[j] = vec[j], vec[j-1]
                k = j
                print(f"BackScan,[{vec[j-1]}<->{vec[j]}] {vec}" )

        # mueve extremo izq de origen
        iz = k+1
        print(f"BackScan Done: {k=}  Range [{iz=},{de=}]" )
        

        # movimiento izquierda-derecha
        for j in range(iz, de+1):
            if vec[j-1] > vec[j]:
                vec[j-1], vec[j] = vec[j], vec[j-1]
                k = j
                print(f"ForwScan Done:,[{vec[j-1]}<->{vec[j]}] {vec}" )
        # mueve extremo dcha de origen
        de = k-1
        print(f"ForwScan, {k=}  Range [{iz=},{de=}]" )
        
    return vec

vec = [ 4,2,6,3,8,1]
shaker_sort(vec)