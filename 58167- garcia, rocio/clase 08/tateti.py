from tablero import draw_tablero, win, full, validate
#draw_tablero(["x", " ", " ", " ", "x", " ", " ", " ", "x"])
tablero=[]
numeros=[]
for i in range(0,9):
    tablero.append(" ")
    numeros.append(str(i+1))
draw_tablero(numeros)
while not win(tablero) and not full(tablero):
    print("turno de la x")
    valido= False
    while not valido:
        print("ingrese una posicion valida de 1 a 9")
        posicion= int(input())
        valido= validate(tablero,posicion)
        if not valido:
            print("error de posicion")
    tablero[posicion-1]= numeros[posicion-1]="x"
    draw_tablero(numeros)
    gano=win(tablero)
    if gano:
        print("gano x")
    else:
        print("turno de la o")
        valido= False
        while not valido:
            print("ingrese una posicion valida de 1 a 9")
            posicion= int(input())
            valido= validate(tablero,posicion)
            if not valido:
                print("error de posicion")
        tablero[posicion-1]= numeros[posicion-1]="o"
        draw_tablero(numeros)
        gano=win(tablero)
        if gano:
            print("gano o")
if full(tablero) and not win(tablero):
    print("nadie gano")