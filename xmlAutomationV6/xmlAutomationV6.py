import random
import string
from threading import Thread

import threading
from contextlib import contextmanager

from string import ascii_uppercase
from random import choice
import os
from string import Template

iteraciones=10000

ficheroDestino="result14.xml"
total=iteraciones*8
generated=0
global_lock = threading.Lock()

# Generar un nombre de carpeta aleatorio
def generate_folder_name():
    # Generar un número aleatorio de caracteres para el nombre de carpeta
    lenght = random.randint(4, 9)
    return ''.join([choice(ascii_uppercase) for i in range(lenght)])

#generar ficheros a partir de plantilla
def generateFiles(templateFile,name):
    
    with open(templateFile,"r") as f:
        temp = f.read()
    template = Template(temp)
    for i in range(iteraciones):
        source_dir=generate_folder_name()
        target_dir=generate_folder_name()
        # Crear el nombre del archivo a partir de las rutas de las carpetas
        filename = f"mover_{name}_application_{source_dir}_{target_dir}.xml"
        global generated
        with global_lock:
            with open(ficheroDestino, "a") as file:
                file.write(filename)
                file.write("\n")
                file.write(template.substitute(ORIGEN=source_dir, DESTINO=target_dir))
                generated += 1
                if (i%5000==0):
                    print(f"{generated}/{total}: Archivo {filename} generado con éxito.")
    
t1 = Thread(target=generateFiles, args=("short_template_doble_pro.xml","archivos_doble_fun1_log"))
t2 = Thread(target=generateFiles, args=("short_template_doble_pro1.xml","archivos_doble_log"))
t3 = Thread(target=generateFiles, args=("short_template_doble_pro2.xml","archivos_doble_fun1"))
t4 = Thread(target=generateFiles, args=("short_template_pro.xml","archivos_simple_fun1_log"))
t5 = Thread(target=generateFiles, args=("short_template_pro1.xml","archivos_simple_log"))
t6 = Thread(target=generateFiles, args=("short_template_pro2.xml","archivos_simple_fun1"))
t7 = Thread(target=generateFiles, args=("short_template_pro3.xml","archivos_simple_fun2"))
t8 = Thread(target=generateFiles, args=("short_template3_pro.xml","archivos_triple_fun1_log"))

# start the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

# wait for the threads to complete
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()


