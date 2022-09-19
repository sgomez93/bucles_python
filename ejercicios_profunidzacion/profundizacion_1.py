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
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números.
Al finalizar el bucle, utilice la variable "cantidad_numeros" y la variable
"sumatoria" para calcular el promedio de todos los números ingresados.
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

# inicio = ....
# fin = ....

inicio = int(input('Ingrese el numero de inicio:\n'))
fin = int(input('Ingrese el numero de Fin:\n'))

# cantidad_numeros ....
# sumatoria ....

cantidad_numeros = 0
sumatoria = 0

# bucle.....

for numero in range(inicio,fin):
    cantidad_numeros += 1
    sumatoria += numero

if numero == (fin-1):
    sumatoria += fin
    cantidad_numeros += 1
    
# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros

promedio = sumatoria / cantidad_numeros

# Imprimir resultado en pantalla
print('La secuencia ingresada tiene', cantidad_numeros, 'numeros y la suma de todos ellos es:', sumatoria)
print('El promedio de la secuencia ingresada es:', promedio)