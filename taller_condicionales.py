# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 09:01:56 2021

@author: amand
"""

# HUA que calcule el total a pagar por la compra de camisas.
# Si se compran tres camisas o mas se aplica un descuento del 30% sobre
# el total de la compra y si son menos de tres camisas un descuento del 10%.

cant = int(input('Digite la cantidad de camisas que desea comprar: '))
precio = int(input('Digite el precio de las camisas: '))
desc = 0
sub_total = cant*precio
if(cant >= 3):
    desc = sub_total*0.30
    print('Usted recibio un descuento del 30%')
else:
    desc = sub_total*0.10
    print('Usted recibio un descuento del 10%')
total = sub_total-desc
print('El total a pagar es: ', total)
print('El descuento realizado fue: ', desc)