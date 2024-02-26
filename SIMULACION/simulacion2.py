#!/usr/bin/env python
#
#Generacion congruencial multiplicativo
#
#Joska Szoke Filatoff
#2024 02 12
#al22760905@ite.edu.mx

import argparse 
import csv
import sys
from enum import Enum

class Errores(Enum):
    PARAMETROA = "El valor de a NO puede ser negativo"
    PARAMETROB = "El valor de b NO puede ser negativo"
    MODULO1 = "El valor de m es negativo"
    SEED = "El valor de la semilla NO puede ser negativo"
    CANTIDAD = "No puede indicar una cantidad negativa por cantidad"
    DECIMALES = "No puede generar una cantidad negativa de decimales"
    MODULO2 = "El valor del modulo no debe ser menor al parametro a, b o semilla"
    
class Aleatorios():
    def _init_(self, parametroA, parametroB, modulo, seed, cantidad, decimales, **kwargs):
        self.parametroA = parametroA
        self.parametroB = parametroB
        self.modulo = modulo
        self.seed= seed
        self.cantidad = cantidad
        self.decimales = decimales
        for key,value in kwargs.items():
            if key == 'a': 
                try: 
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.PARAMETROA.value)
                    sys.exit()
                self.parametroA = value
                
            if key == 'b': 
                try: 
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.PARAMETROB.value)
                    sys.exit()
                self.parametroB = value
            if key == 'm': 
                try: 
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.MODULO1.value)
                    sys.exit()
                self.modulo = value
            if key == 's': 
                try: 
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.SEED.value)
                    sys.exit()
                self.seed = value
            if key == 'n': 
                try: 
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.CANTIDAD.value)
                    sys.exit()
                self.cantidad = value
            if key == 'd': 
                try: 
                    assert (self.validar_decimales(value))
                except AssertionError:
                    print(Errores.DECIMALES.value)
                    sys.exit()
                self.decimales = value
        
        if self.modulo <= self.parametroA or self.modulo <= self.parametroB or self.modulo <= self.seed:
            print(Errores.MODULO2.value)
            sys.exit()
    @staticmethod
    def validar_dato(self, valor):
        return True if valor > 0 else False 
    
    def validar_decimales(self, valor):
        return True if valor >= 0 else False

class GenerarAleatorios():
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
    
    def aleatorios(self):
        pseudoaleatorios = [self.seed]
        for i in range (1, self.cantidad + 1):
            temp = (self.parametroA * pseudoaleatorios[i-1] + self.parametroB) % self.modulo
            pseudoaleatorios.append(temp)
        pseudoaleatorios.pop(0)
        aleatorios = list(map(lambda x: x/self.modulo, pseudoaleatorios))
        return aleatorios

@staticmethod
def crear_archivo(valores):
    data - [] #Unico arreglo con informacion a enviar
    header =['Num','Aleatorio']
    for i in range(len(valores)):
        data.append([i+1, valores[i]])
    with open('simulacion2.vcs', 'w', newLine='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(header)
        writer.writerows(data)
    print("El archivo ha sido creado")

def main(parametroA=161419, parametroB=2022549, modulo=123456789, seed=337719, cantidad= 5, decimales=2, **kwargs):
    iniciar = GenerarAleatorios(parametroA,parametroB,modulo,seed,cantidad,decimales, **kwargs)
    aleatorios = iniciar.aleatorios()
    iniciar.crear_archivo(aleatorios)
    # for aleatorio in aleatorios:
    #    print(aleatorios)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'simulacion2.py',
        formatter_class= argparse.RawDescriptionHelpFormatter, 
        description="""
        Clase para generar valores aleatorios mediante el metodo congruencial
        x_(n+1)= ( ax_n + b ) mod (m)

        Donde:
        a = Valor multiplicativo
        b = Termino independiente
        m = Módulo
        A partit de la semilla XB, el sistema empleará este algoritmo para generar una cantidad de valores (n)
        que posteriormente, serán divididos entre el módulo (m), generando así un arreglo con valores entre [0,1].
        """,
        epilog="""
        En caso de no declarar ningún valor, el programa ya cuenta con valores establecidos por omisión (default).
        """
    )

    parser.add_argument('-a','--terminoA', default=161419,
                        dest="a", help="Valor mulTiplicativo (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-b','--terminoB', default=282549,
                        dest="b", help="Valor independiente (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-m','--modulo', default=123456789,
                        dest="m", help="Módulo (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-s','--seed', default=337719,
                        dest="s", help="Semilla (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-n','--cantidad', default=5,
                        dest="n", help="--Cantidad (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-d','--decimales', default=2,
                        dest="decimales", help="decimales por redondear (default: %(default)s)",
                        type=int, nargs='?', required=False)

#La k es por key y la v por value en el ciclo for
    datos_entrada = {k:value for k,value in vars(parser.parse_args()).items() if value is not None}
    main(**datos_entrada)