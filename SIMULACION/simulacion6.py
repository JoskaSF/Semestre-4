#!/usr/bin/env python
#
#Generacion congruencial multiplicativo
#
#Joska Szoke Filatoff
#2024 02 22
#al22760905@ite.edu.mx

import argparse

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

    #La k es por key y la v por value en el ciclo for
    datos_entrada = {k:value for k,value in vars(parser.parse_args()).items() if value is not None}
    main(**datos_entrada)