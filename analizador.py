import re
import string

# Definir los operadores
operadores = {
    '=': 'Igual a',
    '+': 'Op. Suma',
    '-': 'Op. Resta',
    '/': 'Op. Division',
    '*': 'Op. Multiplicacion'
}
operadores_key = operadores.keys()

# Definir las palabras reservadas
palabras_reservadas = {
    'int': 'variable tipo entero',
    'double': 'variable tipo decimal',
    'string': 'variable tipo cadena',
    'start': 'inicio de codigo',
    'end': 'fin de codigo',
    'var': 'definicion de variable',
    'if': 'condicion if',
    'for': 'bucle for',
    'else': 'condicion else',
    'new': 'nueva asignacion'
}
palabras_reservadas_key = palabras_reservadas.keys()

# Definir los signos
simbolos = {
    '"': 'Inicio y fin de una cadena',
    '<!': 'Inicio de palabra reservada',
    '!>': 'Fin de palabra reservada',
    '(': 'inicio de operacion',
    ')': 'fin de operacion',
    ':': 'Asignacion de variable',
    '#': 'Comentario'
}
simbolos_key = simbolos.keys()

# Definir el abecedario
letras = {letter: 'id' for letter in string.ascii_lowercase}
variables = {letter: 'Nombre variable' for letter in letras if letter not in palabras_reservadas}
variables_key = variables.keys()

# Definir los números
numeros = {i: 'Numero' for i in range(1, 1001)}
numeros_key = numeros.keys()

# Leer el archivo
file = open("read.txt")
a = file.read()

count = 0
program = a.split("\n")
for line in program:
    count += 1
    print(f"Estas en la linea # {count}\n")
    print(f"Contenido: {line}")

    # Usar expresiones regulares para tokenización, incluyendo números decimales
    tokens = re.findall(r'<\!|!\>|\d+\.\d+|\d+|\w+|[^\s\w]', line)
    print("Los elementos son:", tokens)
    print(f"Propiedades de la línea # {count}\n")
    
    for token in tokens:
        if token in operadores_key:
            print(f"{token} es {operadores[token]}")
        elif token in palabras_reservadas_key:
            print(f"{token} es {palabras_reservadas[token]}")
        elif token in simbolos_key:
            print(f'{token} es {simbolos[token]}')
        elif re.match(r'^\d+\.\d+$', token):  # Verificar si es un número decimal
            print(f"{token} es un Número decimal")
        elif token.isdigit() and int(token) in numeros_key:
            print(f"{token} es {numeros[int(token)]}")
        elif token.isalpha():
            print(f"{token} es una cadena de texto")
        else:
            print(f"{token} es un token desconocido o variable no registrada.")
    
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")

file.close()
