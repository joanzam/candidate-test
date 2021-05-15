#!/usr/bin/env python
#!-*- coding: utf-8 -*-

# desarrollado por @joanzamora email: joanzam@gmail.com

""" Este script reemplaza las estructuras de inicializacion inline por la inicializacion 
    soportada de algunas herramientas vendor FPGA.
    
    Tambien exporta el archivo (testcase.v) con los valores de inicializacion y el archivo
    (memdump0.mem) con los valores esperados en la sintaxis soportada. Ambos se encuentran en
    la carpeta (resultados).

 """

# inicializacion
sw = 0
open("resultados/memdump0.mem","w").close()
open("resultados/expected.v","w").close()

# proceso de datos y exportacion
with open('testcase.v') as fname:
    lineas = fname.readlines()
    for linea in lineas:
        linea = linea.strip('\n')
        # exportacion de datos
        if linea.lstrip() == "initial begin":
            print("  $readmemh(\"memdump0.mem\", mem);")
            sw = 1
            # exportacion del expected.v
            with open("resultados/expected.v", "a") as f:
                f.write("  $readmemh(\"memdump0.mem\", mem);"+"\n")
                f.close()
        elif sw == 1 and linea.lstrip() != "end":
            linea = linea[-3:] # obtiene 3 ultimos caracteres
            caracter = ";" # elimina el caracter ";" al final
            for x in range(len(caracter)):
                linea = linea.replace(caracter[x], "")
                print(linea.rstrip())
                # exportacion del memdump0.mem
                with open("resultados/memdump0.mem", "a") as f:
                    f.write(linea.rstrip()+"\n")
                    f.close()
        else:
            if sw == 1 and linea.lstrip() == "end":
                sw = 0
                continue
            else:
                sw = 0
                print(linea)
                # exportacion del expected.v
                with open("resultados/expected.v", "a") as f:
                        f.write(linea+"\n")
                        f.close()