# Complejidad exponencial O(2^N)

import time


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    try:
        numero = int(input('Ingrese número de términos a generar: '))
        if numero <= 0:
            print('El número de términos debe ser mayor o igual a 1')
        else:
            inicio = time.time()
            for i in range(1, numero + 1):
                print('{} => {}'.format(i, fibonacci(i)))
            fin = time.time()
            duracion = fin - inicio
            print('Duración: {} s'.format(duracion))
    except Exception as ex:
        print(str(ex))
