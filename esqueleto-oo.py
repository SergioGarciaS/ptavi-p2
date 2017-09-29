#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Clase(ClaseMadre):
    "Esto es un ejemplo de clase que hereda de ClaseMadre"

    def __init__(self, valor):
        "Esto es el método iniciliazador"
        self.atributo = valor

if __name__ == "__main__":
    objeto = Clase("pepe")
