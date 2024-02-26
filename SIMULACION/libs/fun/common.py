#!/usr/bin/env python
import csv

def validar-los-datos(valor):
    return True if valor > 0 else False

def validar-decimales(valor):
    return True if valor >= 0 else False

def crear-archivos(valores, nombre_archivo):
    data = []
    header = ['Numero','Aleatorio']
    for i in range(len(valores)):
        data.append()