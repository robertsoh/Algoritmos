# Complejidad lineal O(N)

import time


def fibonacci(numero):
    lista = [0, 1]
    for i in range(2, numero + 1):
        lista.append(lista[i - 2] + lista[i - 1])
    return lista


if __name__ == "__main__":
    try:
        numero = int(input('Ingrese número de terminos a generar: '))
        if numero <= 0:
            print('El número de términos debe ser mayor o igual a 1')
        else:
            inicio = time.time()
            lista = fibonacci(numero)
            for i in range(1, numero + 1):
                print('{} => {}'.format(i, lista[i]))
            fin = time.time()
            duracion = fin - inicio
            print('Duración: {} s'.format(duracion))
    except Exception as ex:
        print(str(ex))
