#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class operaciones:
    """ Aquí definimos la clase"""
    def __init__(self,n1,n2):
        self.n1 = num1
        self.n2 = num2
     
     def plus(self):
         return self.n1 + self.n2
        
     def minus(self):
         return self.n1 - self.n2

if __name__ == "__main__":
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        
    calculo = operaciones(op1,op2)
    
    if sys.argv[2] == "suma":
       
    elif sys.argv[2] == "resta":
       
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
