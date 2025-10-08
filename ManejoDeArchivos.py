#Para abrir un archivo utilizaremos open()
archivo=open("./Prueba/txt.txt",'r+')
#Para escribir en un archivo de texto usaremos
#el metodo write()
archivo.write('Primera linea \n')
#Para escribir un numero, lo más común es convertir el número a cadena
numero=5
archivo.write(str(numero))
archivo.seek(0)
print(archivo.read())
archivo.close()
