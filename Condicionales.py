#Condicional if/else
edad=15
trabaja=False
numero=8
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Condicional if/elif/else
if edad<18:
    print("Eres menor de edad")
elif edad<10:
    print ("Eres un niño")
else:
    print ("Eres mayor de edad")

#Condicional multiple
if edad>18 and trabaja==True:
    print ("Eres un adulto")

#Condicional match-case
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