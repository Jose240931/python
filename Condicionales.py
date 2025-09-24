#Condicional if/else
edad=15
trabaja=False
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