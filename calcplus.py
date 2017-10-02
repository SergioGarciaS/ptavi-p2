#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija

if len(sys.argv) != 2:
    sys.exit("Su uso es: python3 calcplus.py fichero")
try:
    calculos = open(str(sys.argv[1]), "r")
    lineas = calculos.readlines()
    calculos.close()
except FileNotFoundError:
    sys.exit("File not found!!")

for operaciones in lineas:
    operaciones = operaciones[:-1].split(",")
    ops = operaciones[1:]
    indice = 0
    resultado = int(ops[0])
    for indice in range(len(ops)-1):
        try:
            num2 = int(ops[indice+1])
        except ValueError:
            sys.exit("Error: Non numerical parameters")
        calculo = calcoohija.CalculadoraHija(resultado, num2)
        if operaciones[0] == "suma":
            resultado = calculo.plus()
        elif operaciones[0] == "divide":
            if num2 != 0:
                resultado = calculo.div()
            else:
                sys.exit("Division by zero is not allowed")
        elif operaciones[0] == "resta":
            resultado = calculo.minus()
        elif operaciones[0] == "multiplica":
            resultado = calculo.multi()
        else:
            sys.exit('Operaciones válidas: suma,resta,multiplica y divide.')

    print(resultado)
