import random
import string
from string import ascii_lowercase
from random import choice
import os
from string import Template

iteraciones=300

ficheroDestino="result11-bis.xml"
total=iteraciones
generated=0

# Generar un nombre de carpeta aleatorio
def generate_folder_name():
    # Generar un número aleatorio de caracteres para el nombre de carpeta
    lenght = random.randint(2, 4)
    return ''.join([choice(ascii_lowercase) for i in range(lenght)])

#generar ficheros a partir de plantilla
def generateFiles(templateFile):
    
    with open(templateFile,"r") as f:
        temp = f.read()
    template = Template(temp)
    for i in range(iteraciones):
        source_dir=generate_folder_name()
        target_dir=generate_folder_name()
        # Crear el nombre del archivo a partir de las rutas de las carpetas
      # filename = f"mover_{name}_application_{source_dir}_{target_dir}.xml"
        global generated
        
        with open(ficheroDestino, "a") as file:
   #         file.write(filename)
    #        file.write("\n")
            file.write(template.substitute(ORIGEN=source_dir, DESTINO=target_dir))
            generated += 1
            if (i%50==0):
                print(f"{generated}/{total}")
    

generateFiles("short_template.xml")

