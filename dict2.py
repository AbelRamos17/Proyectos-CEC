# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:26:10 2022

@author: AbelRamos
"""

dict1={"R1":"10.10.10.1",
       5:"CodigoEMP",
       False:"Estado Civil",
       "R2":"10.10.10.2",
       "R3":"10.10.10.3",
       }
print(dict1)
print(dict1[5])
print(dict1[False])
print(dict1["R1"])
dict1[1]="ESTADO"
print("S2" in dict1)