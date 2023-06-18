import random
import string
from threading import Thread

import threading
from contextlib import contextmanager

from string import ascii_uppercase
from random import choice
import os
from string import Template

iteraciones=20000

ficheroDestino="result13.xml"
total=iteraciones*3
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
    
t1 = Thread(target=generateFiles, args=("short_template.xml","archivos_simple"))
t2 = Thread(target=generateFiles, args=("short_template2.xml","archivos_doble"))
t3 = Thread(target=generateFiles, args=("short_template3.xml","archivos_triple"))


# start the threads
t1.start()
t2.start()
t3.start()


# wait for the threads to complete
t1.join()
t2.join()
t3.join()



