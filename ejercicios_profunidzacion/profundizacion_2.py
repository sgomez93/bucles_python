# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

operacion = 'ok'
operador = 0

while(operacion != 'fin'):
    if(operador == 0):
        numero_1 = int(input('Ingrese el primer numero:\n'))
        numero_2 = int(input('Ingrese el segundo numero:\n'))
        print('Ingrese operacion desea hacer colocando el simbolo, de la siguiente manera:')
        print(' 1- Suma(+)\n','2- Resta(-)\n','3- Multiplicacion(*)\n','4- Division(/)\n','5- potencia(**)\n')

    operacion = str(input())

    if (operacion == '+'):
        valor = numero_1 + numero_2
        operador = 0 # coloco de nuevo operador a 0 para que funcione correctamente la calculadora
        print('La suma de {} + {} es igual a {}'.format(numero_1, numero_2, valor))
    elif (operacion == '-'):
        valor = numero_1 - numero_2
        operador = 0 # coloco de nuevo operador a 0 para que funcione correctamente la calculadora
        print('La resta de {} - {} es igual a {}'.format(numero_1, numero_2, valor))
    elif(operacion == '*'):
        valor = numero_1 * numero_2
        operador = 0 # coloco de nuevo operador a 0 para que funcione correctamente la calculadora
        print('La multiplicacion de {} * {} es igual a {}'.format(numero_1, numero_2, valor))
    elif(operacion == '/'):
        valor = numero_1 / numero_2
        operador = 0 # coloco de nuevo operador a 0 para que funcione correctamente la calculadora
        print('La division de {} * {} es igual a {}'.format(numero_1, numero_2, valor))
    elif(operacion == '**'):
        valor = numero_1 ** numero_2
        operador = 0 # coloco de nuevo operador a 0 para que funcione correctamente la calculadora
        print('La potencia de {} a la {} es igual a {}'.format(numero_1, numero_2, valor))
    elif (operacion != 'fin'):
        print('Debe colocar uno de los operadores anteriores o la palabra fin')
        operador = 1 # variable para darme cuenta si ingresaron un operardor mal y que solo pida el operardor correcto

print('Termino la calculadora!!!')

    








