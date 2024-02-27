#!/usr/bin/env python
#
#Generacion congruencial multiplicativo
#
#Joska Szoke Filatoff
#2024 02 22
#al22760905@ite.edu.mx

import sys
import argparse
# import numpy as np
from libs.fun.common import validar_dato, validar_intervalo

class utilidad(object):
    def __init__(self,dias, semanas, anios, decimales, **kwargs):
        self.dias = dias
        self.semanas = semanas
        self.anios = anios
        self.decimales = decimales
        for key, value in kwargs.item():
            if key == 'precio':
                try:
                    assert (validar_dato(value[0]))
                except AssertionError:
                    print('el precio no puede ser negativo')
                    sys.exit()
                self.precio = value[0]
            if key == 'productos':
                venta_minima = value[0]
                venta_maxima = value[1]
                try:
                    assert(validar_dato(venta_minima))
                except AssertionError:
                    print('el minimo de la venta estimada no puede ser negativo')
                    sys.exit()
                try:
                    assert(validar_dato(venta_maxima))
                except AssertionError:
                    print('el maximo de la venta estimada no puede ser negativo')
                    sys.exit()
                try:
                    assert(validar_intervalo(venta_maxima, venta_minima))
                except AssertionError:
                    print('')
                    sys.exit()


class CalculoUtilidad(Utilidad):
    def __init__(self, * args, **kwargs):
        super().__init__(*args,**kwargs)

def main(**kwargs):
    # Numero de dias de la simulacion
    dias = 7
    # Numero de semanas para la simulacion
    semanas = 52
    # anios que dura la simulacion
    anios = 5
    # Cantidad de decimales por emplear
    decimales = 2
    CalculoUtilidad(dias, semanas, anios, decimales, **kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'simulacion6.py',
        formatter_class= argparse.RawDescriptionHelpFormatter, 
        description="""
        Obtener la utilidad estimada de la venta de un producto

        """,
        epilog="""
        La salida de los resultados se almacenara en el archivo simulacion4.csv
        """
    )

    parser.add_argument('-p','--precio',
                        dest="precio", help="Precio del producto",
                        type=float, nargs=1, required=True)

    parser.add_argument('-v','--venta',
                        dest="productos", help="Venta estimada",
                        type=int, nargs=2, required=True)

    parser.add_argument('-d','--dias', default=7,
                        dest="d", help="Dias de la simulacion (default: %(default)s=)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-s','--semanas', default=52,
                        dest="s", help="Semanas de la simulacion (default: %(default)s=)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-y','--year', default=5,
                        dest="yrs", help="Years de la simulacion (default: %(default)s=)",
                        type=int, nargs='?', required=False)

    #La k es por key y la v por value en el ciclo for
    datos_entrada = {key:value for key,value in vars(parser.parse_args()).items() if value is not None}
    # main(**datos_entrada)