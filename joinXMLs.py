import glob
import os

read_files = glob.glob("./xmls5/*.xml")

with open("result10.xml", "wb") as outfile:
    for f in read_files:
        outfile.write(bytes(os.path.basename(f),'utf-8'))
        with open(f, "rb") as infile:
            outfile.write(infile.read())
