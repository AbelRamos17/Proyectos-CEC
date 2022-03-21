# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 01:42:44 2022

@author: AbelRamos
"""

def direct(ciudad,barrio,calle):
    print("La dirrecion de entrega es: ")
    print("Ciudad: ",ciudad)
    print("La referencia es: ",barrio)
    print("La entrega sera en la calle: ", calle)
    
ca=input("Ingrese la calle: ")
ci=input("Ingrese la ciudad: ")
ba=input("Ingrese el barrio o sector: ")

direct(ci, ba, ca)