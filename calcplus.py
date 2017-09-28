#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

calculos = open(str(sys.argv[1]), "r")
lineas = calculos.readlines()
calculos.close()

for operaciones in lineas:
    operaciones = operaciones[:-1].split(",")
    ops = operaciones[1:] #Hasta aquí el troceador.
    
    print(operaciones[0])
    indice = 0
    resultado = int(ops[0])
    for indice in range(len(ops)-1):

        if operaciones[0] == "suma":
            resultado = resultado +int(ops[indice+1])
        elif operaciones[0] == "resta":
            resultado = resultado -int(ops[indice+1])
        elif operaciones[0] == "divide":
            resultado = resultado /int(ops[indice+1])
        elif operaciones[0] == "multiplica":
            resultado = resultado *int(ops[indice+1])
        else:
            sys.exit('Operaciones válidas: suma,resta,multiplica y divide.')
            
    print(resultado)
