import zipfile
import os

ruta = 'extract'

def mapear ():
    contenido = os.listdir(ruta)
    contenido.sort(key=len)
    return contenido

def extraer():
    ctf_extract = zipfile.ZipFile(ruta + '\\' + mapear()[0])
    ctf_extract.extractall(ruta)
    ctf_extract.close()

def ejecutar():
    extraer()
    while(mapear()[1].endswith(".zip")):
        extraer()
        os.remove(ruta + '\\' + mapear()[1])
    os.remove(ruta + '\\' + mapear()[0])
    print('FLAG ENCONTRADA')

ejecutar()
