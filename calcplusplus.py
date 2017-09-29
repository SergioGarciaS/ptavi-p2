#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija
import csv

with open(sys.argv[1]) as calculos:
    entrada = csv.reader(calculos)
    for operaciones in entrada:
        ops = operaciones[1:]
        print(operaciones[0])
        indice = 0
        resultado = int(ops[0])
        for indice in range(len(ops)-1):
            num2 = int(ops[indice+1])
            calculo = calcoohija.calculadorahija(resultado, num2)
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
                sys.exit('Operaciones válidas:suma,resta,multiplica y divide.')

        print(resultado)
