#!/usr/bin/env python
#
#Generacion congruencial multiplicativo
#
#Joska Szoke Filatoff
#2024 02 12
#al22760905@ite.edu.mx

import argparse
import datetime
import sys
import libs.fun.common import validar_los_datos, validar_decimales, crear_archivo
from libs.classes.Errores3 import Errores3

class aleatorios(object):
    def __init__(self.parametrot, bandera, cantidad, decimales, **kwargs):
        self.parametrot = parametrot
        self.bandera = bandera
        self.cantidad = cantida
        self.decimales = decimales
        for key, value in kwargs.items():
            if key == "intervalo":
                valor_minimo = value[0]
                valor_maximo = value[1]
                if valor_minimo >= valor_maximo:
                    print(Errores3.INTERVALO.value)
                    sys.exit()
                self.valor_minimo = valor_minimo
                self.valor_maximo = valor_maximo
            if key == "t":
                try:
                    assert(validar_los_datos(value))
                except AssertionError:
                    print(Errores3.PARAMETROT.value)
                    sys.exit()
                self.parametrot = value
            if key == "b":
                self.bandera = value
            if key == "n":
                try:
                    assert(validar_los_datos(value))
                except AssertionError:
                    print(Errores3.CANTIDAD.value)
                    sys.exit()
                self.cantidad = value
            if key == "d":
                try:
                    assert(validar_los_datos(value))
                    except AssertionError:
                        print(Errores3.DECIMALES.value)
                        sys.exit()
                    self.decimales = value

class CrearIntervalo(Aleatorios):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def crear-aletorios(self):
        ahora = datetime.datetime.now()
        semilla = ahora.microsecond
        pseudoaleatorios = [semilla]
        valor_a = 8 * self.parametrot + (self.bandera * 3)
        modulo = 2 ** 31
        for i in range(1, self.cantidad + 1):
            temp = (valor_a * pseudoaleatorios[i - 1]) % modulo
            pseudoaleatorios.append(temp)
        pseudoaleatorios.pop(0)
        aleatorios = list(map(lambda x: x / modulo, pseudoaleatorios))
        return aleatorios

    def valores-intervalo(self):
        aleatorios = self.crear_aleatorios()
        c = (self.valor_maximo - self.valor_minimo)
        valores-intervalo = list(
            map(
                lambda y: round(c * y + self.valor.valor_minimo, selg.decimales),
                aleatorios
            )
        )            
        return valores_intervalo


def main(**kwargs):
    parametrot = 337719
    bandera = 1
    cantidad = 6
    decimales = 3
    iniciar = CrearIntervalo(*args, parametrot, bandera, cantidad, decimales, **kwargs)
    valores = iniciar.valores_intervalo()
    nombre_archivo = "simulacion.csv"
    crear_archivo(valores, nombre_archivo)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'simulacion3.py',
        formatter_class= argparse.RawDescriptionHelpFormatter, 
        description="""
        Generar valores en el intervalo [a,b] empleando el generador
        congruencial multiplicativo
                                    x_(n+1) = (ax_n) mod (m)
        Donde:
        a = 8t +/- 3
        m = 2 ** 31
        El usuario debera indicar el inicio y el fin del intervalo en la forma 
                            simulacion.py --intervalo a,b
        Opcionalmente se podra indicar la cantida de valores aleatorios por
        ser generados, asi como la cantidad de decimales por emplear
        """,
        epilog="""
        La salida de los resultados se almacenara en el archivo simulacion3.csv
        """
    )

    parser.add_argument('-i','--intervalo',
                        dest="intervalo", help="Intervalo por ser generado",
                        type=float, nargs=2, required=True)

    parser.add_argument('-t','--parametroT', default=337719,
                        dest="t", help="Parametro del generador (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-b','--bandera', default=1, choices=[1, -1],
                        dest="b", help="Indicar como 1 si es resta (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-n','--cantidad', default=5,
                        dest="n", help="--Cantidad (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-d','--decimales', default=2,
                        dest="decimales", help="decimales por redondear (default: %(default)s)",
                        type=int, nargs='?', required=False)

#La k es por key y la v por value en el ciclo for
    datos_entrada = {key:value for key,value in vars(parser.parse_args()).items() if value is not None}
    main(**datos_entrada)