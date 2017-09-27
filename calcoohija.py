#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class calculadorahija(calcoo.calculadora):
    """ Aquí definimos la clase"""
    def multi(self):
        return self.n1 * self.n2
    def div(self):
        try:
            return self.n1 / self.n2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
if __name__ == "__main__":
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    calculo = calculadorahija(op1, op2)
    if sys.argv[2] == "suma":
        result = calculo.plus()
    elif sys.argv[2] == "resta":
        result = calculo.minus()
    elif sys.argv[2] == "multiplica":
        result = calculo.multi()
    elif sys.argv[2] == "divide":
        result = calculo.div()
    else:
        sys.exit('Operaciones válidas: suma,resta,multiplica y divide.')
    print(result)

