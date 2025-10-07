
#Se intenta hacer algo con el try, en este caso capturar un numero, y dividirlo entre cero
try:
    valor = int(input("Introduce un numero: "))
    print(valor/0)

#Con raise al igual que en java se lanzan excepciones manualmente
    raise Exception

#Se asocia una posible excepcion que es valueError la cual avisa que se ha introducido un valor erroneo
except ValueError:
    print("Ha ocurrido un error en la ejecucion del codigo")
#Se pueden añadir varias excepciones a un mismo try en este caso esta excepcion
# hace referencia a la division entre cero
except ZeroDivisionError:
    print("Error: se ha intentado dividir entre cero")
#Esta es una excepcion general, es decir se crea una variable que va a ser la que se guarde el error de ejecucion
except Exception as error:
    print("Se ha producido un error:", error)
#Al poner else despues de un try, solo se ejecuta lo de dentro del else si no se lanza ninguna excepcion
else:
    print("No se ha producido un error")
#Con finally hacemos que se ejecuta algo despues del try and catch, esto es igual que en java
finally:
    print ("Este es el final del programa")
