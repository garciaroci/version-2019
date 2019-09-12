from generador import generador, generador_mejor
buscado= generador(1, 1000)
adivinado = False
lista=[]
while adivinado == False:
    print("ingrese un numero")
    num=int(input())
    if num==buscado:
        print("adivinaste")
        adivinado = True
    if num<buscado:
        print("es mayor")
    if num>buscado:
        print("es menor")
    if adivinado == False:
        num2= generador_mejor(1, 1000, lista)
        lista.append(num2)
        if num2==adivinado:
            print("adivino pc")
            adivinado = True

