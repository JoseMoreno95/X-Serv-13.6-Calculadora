#!/usr/bin/python3

import sys

if len (sys.argv) != 4:
    print ('¡No has introducido el número correcto de argumentos!')
    print ('El formato es: ./calculadora.py <operador> <número1> <número2>')
    sys.exit(1)
try:
    number1 = float (sys.argv[2])
    number2 = float (sys.argv[3])
except ValueError:
    print ('¡No has introducido dos números válidos!')
    print ('El formato es: ./calculadora.py <operador> <número1> <número2>')
    sys.exit(1)

try:
    if sys.argv[1] == '+':
        result = number1 + number2
    elif sys.argv[1] == '-':
        result = number1 - number2
    elif sys.argv[1] == '*':
        result = number1 * number2
    elif sys.argv[1] == '/':
        if number2 == 0:
            print ('¡Error! División por 0.')
            sys.exit(1)
        else:
            result = number1 / number2
    else:
        raise Exception
except Exception:
    print('¡No has introducido un operador válido! (+ - \* /)')
    sys.exit(1)

print ('La operación es: ', number1, ' ', sys.argv[1], ' ', number2, ' = ', result)
sys.exit(0)
