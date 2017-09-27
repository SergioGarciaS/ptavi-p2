#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class calculadora(calcoo.calculdora):
    """ Aquí definimos la clase"""
     
    def multi(self):
        return self.n1 * self.n2
        
    def div(self):
        try:
            return self.n1 / self.n2
        except ZeroDivisionError:
            print("Division by zero is not allowed")

if __name__ == "__main__":
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        
    calculo = calculadora(op1,op2)
    
    if sys.argv[2] == "suma":
       result = calculo.plus()
    elif sys.argv[2] == "resta":
       result = calculo.minus()
    elif sys.argv[2] == "multiplica":
       result = calculo.multi()
    elif sys.argv[2] == "divide":
       result = calculo.div()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
