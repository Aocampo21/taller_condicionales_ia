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
valor_cuota = 0
if (monto < 50000):
    valor_cuota = monto*0.03
    print('Usted debe pagar el 3% de la cuota a financiar', valor_cuota)
else:
    valor_cuota = monto*0.02
    print('Usted debe pagar el 2% de la cuota a financiar', valor_cuota)
cuota_total = int(input(f'La cuota a pagar es: {valor_cuota + monto}'))

# Una fábrica ha sido sometida a un programa de control de contaminación para
# lo cual se efectúa una revisión de los puntos de contaminación generados
# por la fábrica. El programa de control de contaminación consiste en medir
# los puntos que emite la fábrica en cinco días de una semana y si el promedio
# es superior a los 170 puntos entonces tendrá la sanción de parar su
# producción por una semana y una multa del 50% de las ganancias diarias
# cuando no se detiene la producción. Si el promedio obtenido de puntos es de
# 170 o menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la revisión.

dia1 = int(input('Digite los puntos que emitio la fabrica el día 1: '))
dia2 = int(input('Digite los puntos que emitio la fabrica el día 2: '))
dia3 = int(input('Digite los puntos que emitio la fabrica el día 3: '))
dia4 = int(input('Digite los puntos que emitio la fabrica el día 4: '))
dia5 = int(input('Digite los puntos que emitio la fabrica el día 5: '))
promedio_puntos = float(dia1+dia2+dia3+dia4+dia5)/5
ganancia = int(
    input('Ingrese las ganancias obtenidas en un día normal de produccion: '))
if (promedio_puntos > 170):
    multa = ganancia*0.50
    print('Usted debe parar la producción por una semana y pagar una multa del'
          ' 50% sobre las ganancias diarias, el promedio obtenido es: ',
          promedio_puntos)
else:
    print('Usted no tiene sanción, ni multa. El promedio obtenido es: ',
          promedio_puntos)
print('El valor a pagar diario sera: ', multa)
perdida_semana = int(input(f'La perdida total será: {multa * 5}'))

# Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.

precio = int(input('Ingrese el valor del automóvil y del terreno: '))
incremento = int(input('Ingrese el incremento anual del terreno: '))
devaluacion = int(input('Ingrese la devaluación anual del automóvil: '))
incr = float(((precio*incremento)/100)*3)/2
print('La mitad del incremento del costo del terreno en 3 años será: ',
      incr)
deva = int((precio*devaluacion)/100)*3
print('La devaluación del automóvil en 3 años será: ', deva)
if(deva < incr):
    print('Usted debe comprar el automóvil')
else:
    print('No debe comprar el automóvil')

# En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.

num = int(input('Ingrese el número de computadores que desea comprar: '))
sub_total = num*11000
desc = 0
if (num < 5):
    desc = sub_total*0.10
elif (num < 10):
    desc = sub_total*0.20
else:
    desc = sub_total*0.40
print('Usted recibio un descuento de: ', desc)
print('El total a pagar es: ', sub_total - desc)

# Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.

precio = int(input('Digite el precio del aparato: '))
precio_iva = precio*1.16
if(precio >= 2000):
    marca = str(input('Digite la marca del aparato: '))
    if(marca == "NOSY"):
        desc = precio*0.10
        sun_total = precio_iva - desc
        desc2 = sub_total*0.05
        total = sub_total - desc2
        print('El total a pagar es: ', total)
    else:
        desc = precio*10
        total = precio_iva - desc
        print('El total a pagar es: ', total)
else:
    print(f'El total a pagar es:{precio_iva}, No se le aplica descuento')

# Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.00 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses.

num_piezas = int(input('Ingrese el número de piezas: '))
costo_pieza = int(input('Ingrese el costo de la pieza: '))
total = num_piezas*costo_pieza
if(total > 500000):
    inver_empresa = total*0.55
    banco = total*0.30
    print('Usted recibio un prestamo por parte del banco de: ', banco)
    credito = total*0.70
else:
    inver_empresa = total*0.70
    credito = total*0.30
    print('Usted no recibio un prestamo de parte del banco')
interes = credito*0.20
print('Usted debe invertir: ', inver_empresa)
print('Obtuvo un credito por: ', credito)
print('Por intereses debe pagar: ', interes)

# Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume.

num_uno = float(input('Digite el primer número'))
num_dos = float(input('Digite el segundo número'))
if(num_uno == num_dos):
    resultado = num_uno*num_dos
    print('Los números son iguales, por lo tanto se multiplican')
    print('El resultado es: ', resultado)
elif (num_uno > num_dos):
    resultado = num_uno - num_dos
    print('El primer número es mayor, por lo tanto se hara una resta')
    print('El resultado es:', resultado)
else:
    resultado = num_uno + num_dos
    print('El primer número es menor, por lo tanto se hara una suma')
    print('El resultado es: ', resultado)
        



    
        
