#!/usr/bin/env python
#
#Generar calificaciones con calificacion aleatoria
#
#Joska Szoke Filatoff
#2024 02 22
#al22760905@ite.edu.mx

import argparse
import sys
from libs.classes.Errores3 import Errores3
# from libs.

class Validar(object):
    def __init__(self,arametrot, bandera, decimales, modulo, **kwargs):
        self.parametrot = parametrot
        self.bandera = bandera
        self.decimales = decimales
        self.modulo = modulo
        for key, value in kwargs.item():
            if key == "intervalo":
                valor_minimo = value[0]
                valor_maximo = value[1]
                if valor_minimo >= valor_maximo:
                    print(Errores3.INTERVALO.value)
                    sys.exit()
                self.valor_maximo = valor_maximo
                self.valor_minimo = valor_minimo
            if key == "alumnos":
                try:
                    assert (validar_dato(value[0]))
                except:
                    


class GenerarCalificaciones(Validar):
    def __init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)

def main(**kwargs):
    parametrot = 4395136
    bandera = 1
    decimales = 0
    modulo = 2 ** 31
    iniciar = GenerarCalificaciones(parametrot,bandera,decimales,modulo, **kwargs)
    # valores = iniciar.valores_intervalo()
    # nombre_archivo
    # 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'simulacion3.py',
        formatter_class= argparse.RawDescriptionHelpFormatter, 
        description="""
        Crear calificaciones en la escala determinada por el usuario, donde
        se reporbara de forma aleatoriia.
        Para ello, se deberan de indicar como datos, la escala aprobatoria,
        asi como el numero de estudianes.
        Por ejemplo
                            --esala 6 10 --alumnos 10
        """,
        epilog="""
        La salida de los resultados se almacenara en el archivo simulacion4.csv
        """
    )

    parser.add_argument('-i','--intervalo',
                        dest="intervalo", help="Intervalo por ser generado",
                        type=int, nargs=2, required=True)

    parser.add_argument('-n','--alumnos',
                        dest="alumnos", help="Indicar cantidad de alumnos en la clase",
                        type=int, nargs=2, required=True)

    #La k es por key y la v por value en el ciclo for
    datos_entrada = {k:value for k,value in vars(parser.parse_args()).items() if value is not None}
    main(**datos_entrada)