import random
def generador(minimo, maximo):
    return random.randint(minimo,maximo)
if __name__ == "__main__":
    print(generador(1,20))