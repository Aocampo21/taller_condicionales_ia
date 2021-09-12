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
print('El descuento realizado es: ', desc)

# En un supermercado se hace una promoción, mediante la cual el cliente
# obtiene un descuento dependiendo de un número que se escoge al azar.
# Si el número escogido es menor que 74 el descuento es del 15% sobre el
# total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

compra = int(input('Digite el valor de la compra: '))
num = int(input('Digite un número: '))
desc = 0
if(num < 74):
    desc = compra*0.15
    print('Usted recibio un descuento del 15%')
else:
    desc = compra*0.20
    print('Usted recibio un descuento del 20%')
total = compra - desc
print('El descuento aplicado es: ', desc)
print('El total a pagar es: ', total)


# Una compañía de seguros está abriendo un departamento de finanzas y
# estableció un programa para captar clientes, que consiste en lo sgte: Si el
# el monto por el que se efectúa la fianza es menor que $50.000 la cuota a
# a pagar será por el 3% del monto, y si el monto es mayor que $50.000
# la cuota a pagar será el 2% del monto. La afianzadora desea
# determinar cual será la cuota que debe pagar al cliente.

monto = int(input('Digite el monto que desea financiar: '))
valor_financiar = 0
if (monto < 50000):
    valor_cuota = monto*0.03
    print('Usted debe pagar el 3% de la cuota a financiar', valor_cuota)
else:
    valor_cuota = monto*0.02
    print('Usted debe pagar el 2% de la cuota a financiar', valor_cuota)
cuota_total = int(input(f'La cuota a pagar es: {valor_cuota + monto}'))



            
