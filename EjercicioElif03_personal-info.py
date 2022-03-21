# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:44:43 2022

@author: AbelRamos
"""

Nombre=input("Escriba su nombre:")
Apellido=input("Escriba su apellido:")
edad=int(input("Escriba su edad:"))
Ciudad=input("Ingrese su ciudad:")
space=" "
if edad>=1 and edad<=10:
    print("Es un niño")
elif edad>=11 and edad<=17:
    print("Es un adolescente")
elif edad>=18 and edad<=60:
    print("Es un adulto")
else:
    print("Es un adulto mayor")
    

print("¡Hola!", Nombre, Apellido, "hoy cumples",edad,"años, felicidades", "tu pedido esta listo y entregado en la ciudad de",Ciudad, )