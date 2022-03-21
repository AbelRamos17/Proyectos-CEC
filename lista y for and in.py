# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:09:13 2022

@author: AbelRamos
"""
switch=[]
lista=["R1","R2","R3","R4","R5","S1","S2"]
for item in lista:
    if "S" in item:
        switch.append(item)
        
print(switch)
    