import random
import string
from threading import Thread

import threading
from contextlib import contextmanager

from string import ascii_letters, digits
from random import choice
import os
from string import Template

iteraciones=50000
rutaDestino="/gpt/xmls5/"
ficheroDestino="result10.xml"
total=iteraciones*4
generated=0
global_lock = threading.Lock()

# Generar un nombre de carpeta aleatorio
def generate_folder_name():
    # Generar un número aleatorio de caracteres para el nombre de carpeta
    lenght = random.randint(2, 15)
    return ''.join([choice(ascii_letters + digits) for i in range(lenght)])

#generar ficheros a partir de plantilla
def generateFiles(templateFile,name):
    
    with open(templateFile,"r") as f:
        temp = f.read()
    template = Template(temp)
    for i in range(iteraciones):
        source_dir=generate_folder_name()
        target_dir=generate_folder_name()
        # Crear el nombre del archivo a partir de las rutas de las carpetas
        filename = f"{rutaDestino}mover_{name}_application_{os.path.basename(source_dir)}_{os.path.basename(target_dir)}.xml"
        global generated
        with global_lock:
            with open(ficheroDestino, "a") as file:
                file.write(filename)
                file.write("\n")
                file.write(template.substitute(ORIGEN=source_dir, DESTINO=target_dir))
                generated += 1
                if (i%5000==0):
                    print(f"{generated}/{total}: Archivo {filename} generado con éxito.")
    
t1 = Thread(target=generateFiles, args=("template_simple.xml","archivos_simple"))
t2 = Thread(target=generateFiles, args=("template_doble.xml","archivos_doble"))
t3 = Thread(target=generateFiles, args=("template_triple.xml","archivos_triple"))
t4 = Thread(target=generateFiles, args=("template_multiple.xml","archivos_multiple"))

# start the threads
t1.start()
t2.start()
t3.start()
t4.start()

# wait for the threads to complete
t1.join()
t2.join()
t3.join()
t4.join()


