from generador import generador 
adivinado = False
aleatorio = generador(1, 20)
while adivinado == False:
    print("ingrese un numero entre 1 y 20")
    numero=int(input())
    if numero==aleatorio:
        print("adivinaste")
        adivinado= True
    if numero < aleatorio:
        print("ingresa uno mas grande")
    if numero > aleatorio:
        print("es mas chico")