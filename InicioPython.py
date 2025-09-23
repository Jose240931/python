import random

#pedir edad del usuario
edad=int (input ("Introduce tu edad"))

#Le sumo 10 a la edad que es introducida por el usuario
edad +=10

#Habiendo previamente importado la libreria random, uso la funcion de obtener un numero aleatorio entre 1 y 10
numero=random.randint(1,10)

#Hago un match case que busca el numero aleatorio obtenido anteriormente
match numero:
    case 1:
        print("Seras medico y tendras ",edad," años")
    case 2:
        print ("Seras piloto y tendras  ",edad," años")
    case 3:
        print ("Seras profesor y tendras ",edad," años")
    case 4:
        print ("Seras programador y tendras ",edad," años")
    case 5:
        print ("Seras bombero y tendras ",edad," años")
    case 6:
        print ("Seras policia y tendras ",edad," años")
    case 7:
        print ("Seras ingeniero y tendras ",edad," años")
    case 8:
        print("Seras mecanico y tendras ",edad," años")
    case 9:
        print("Seras diseñador 3d y tnedras ",edad," años")
    case 10:
        print("Seras militar y tendras ",edad," años")
#Finalmente se habrá impreso en pantalla alguno de los case anteriores mostrando 10 años mas de la edad introducida
#y un trabajo aleatorio