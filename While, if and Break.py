# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:41:45 2022

@author: AbelRamos
"""
while True:
    numero=input("Ingrese el # al que contare: ")
    if numero == "q" or numero == "quit":
        break
    numero=int(numero)
    contador=1
    while True:
        print(contador)
        contador+=1
        if contador>numero:
            break
    


