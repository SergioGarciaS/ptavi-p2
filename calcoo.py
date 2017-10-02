#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:
    """ Aquí definimos la clase"""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def plus(self):
        return self.n1 + self.n2

    def minus(self):
        return self.n1 - self.n2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Su uso es: python3 calco0.py num1 operación num2")
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculo = Calculadora(op1, op2)

    if sys.argv[2] == "suma":
        result = calculo.plus()
    elif sys.argv[2] == "resta":
        result = calculo.minus()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
