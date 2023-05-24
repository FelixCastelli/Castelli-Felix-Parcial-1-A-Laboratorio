import os
from menu_opciones_administracion_insumos import *

ruta_csv = "D:\\Usuarios\\mylov\\Escritorio\\UTN\\Castelli Felix Parcial 1-A Laboratorio\\Primer Parcial\\insumos.csv"
ruta_json = "D:\\Usuarios\\mylov\\Escritorio\\UTN\\Castelli Felix Parcial 1-A Laboratorio\\Primer Parcial\\lista_alimentos.json"
ruta_txt = "D:\\Usuarios\\mylov\\Escritorio\\UTN\\Castelli Felix Parcial 1-A Laboratorio\\Primer Parcial\\marcas.txt"

lista_csv = []
lista_dict_transformada = []
lista_alimentos = []
flag_lista_csv = False
flag_lista_json = False

while True:
    os.system("cls")
    opcion = menu_opciones()
    os.system("cls")

# Verifica que si ingresa la opcion 10 y la cancele pueda seguir ingresando la opcion 1 para poder hacer las demas opciones y que si no ingresa la 1 no funcionen las demas menos la 10
    if opcion == 12 or (opcion == 1 and not flag_lista_csv):
        flag_lista_csv = True

    elif not flag_lista_csv:
        os.system("cls")
        print("ERROR, La lista no está creada. Por favor, cree la lista antes de continuar")
        os.system("pause")
        continue

    if opcion == 7:
        flag_lista_json = True

    elif opcion == 8 and not flag_lista_json:
        os.system("cls")
        print("ERROR, La lista de alimentos no está creada. Por favor, cree la lista antes de continuar")
        os.system("pause")
        continue

    opcion_salir, lista_csv, lista_dict_transformada, lista_alimentos = elegir_opcion(opcion, ruta_csv, lista_csv, lista_dict_transformada, lista_alimentos, ruta_json, ruta_txt)
    if opcion_salir == 's':
        os.system("cls")
        break
    os.system("pause")