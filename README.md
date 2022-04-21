# Presentación del reto
Muchas veces comprimir un archivo zip nos ayuda a reducir el tamaño de un archivo, pero en este caso será todo lo contrario. Dentro de este archivo .zip se encuentra la **FLAG** para resolver este reto, pero para poder llegar a ellá deberás deberás hallar la aguja dentro de un pajar. 

Pista: Utiliza tu lenguaje favorito para hacerlo.
# Solucionario
Para la solución se utilizó un script codificado en Python el cual ocupa dos librerías:
* ZipFile
* OS

### ZipFile
Es una librería utilizada para trabajar con archivos Zip utilizando Python como lenguaje.

### OS
Es una librería utilizada para trabajar con archivos y directorios utilizando Python como lenguaje.

## Solución en código
1. Como primer paso se importan las librerías a utilizar en nuestro archivo .py
~~~
import zipfile
import os
~~~
2. Se crea una variable con la ruta de la carpeta con la cual se trabajará (esta puede ser absoluta o relativa)
~~~
ruta = 'extract'
~~~
3. Se genera el método `mapear()` el cual devuelve un arreglo con los nombres de los archivos que se encuentran en la variable `ruta`
~~~
def mapear ():
    contenido = os.listdir(ruta)
    contenido.sort(key=len)
    return contenido
~~~
4. Posteriormente creamos el método `extraer()` en el cual creamos una instancia del objeto ZipFile que nos otorga la librería ZipFile. En este método se encuentra la lógica para extraer la información dentro de un archivo zip que se encuentra dentro del archivo que se encuentra en la pocisión 0 de nuestro directorio de trabajo.
~~~
def extraer():
    ctf_extract = zipfile.ZipFile(ruta + '\\' + mapear()[0])
    ctf_extract.extractall(ruta)
    ctf_extract.close()
~~~
5. Luego se crea el método `ejecutar()` el cual es el encargado de extraer de forma recursiva los archivos zip. En este método primero se ejecuta el método `extraer()` para obtener el segundo archivo zip de el grupo el cual se ubicará en la pocisión 1 de nuestro método `mapear()[1]`. Posteriormente se ingresa a un ciclo `while` en cuya condición verificamos que el archivo que se encuentre en la pocisión 1 del método `mapear()[1]` sea en efecto un archivo zip y que este termine cuando en esa pocisión se encuentre un archivo diferente a un zip. Posteriormente procedemos  a eliminar este archivo para evitar generar archivos basura. Una vez culminado el ciclo este método muestra por pantalla el mensaje **FLAG ENCONTRADA** y procede a eliminar el último archivo basura generado.
~~~
def ejecutar():
    extraer()
    while(mapear()[1].endswith(".zip")):
        extraer()
        os.remove(ruta + '\\' + mapear()[1])
    os.remove(ruta + '\\' + mapear()[0])
    print('FLAG ENCONTRADA')
~~~