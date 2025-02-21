#CONDICIONALES/CONDITIONALS:
#Los condiciones nos representa la manera de establecer flujos de ejecución de nuestro código ->Decide si algo de nuestro código se ejecuta.
#Si se cumple una condicipon yo ejecuto lo que está dentro de la condicional.

#Dato.-Para lograr entender una condicional tenemos el tipo de dato boleanos/bolean.
#Dato.-Se escribe con la palabra reserva if

#1.-Creación de variable
#Si es True se ejecuta y si es Flase no se ejecuta
my_condition = True

if my_condition:  #Como la variable tiene el valor de True pasa e imprime.
    print('Se ejecuta la condición del if')

print('La ejecución continúa')


my_condition = 5 * 5 #No está cumpliendo ya que esto no es ni un True o False entonces nos lo da como bueno y por eso pasa.

if my_condition:  
    print('Se ejecuta la condición del segundo if')

print('La ejecución continúa')

if my_condition ==11 :  #Acá le estamos asigando lo que debe de evaluar para el True o False.
    print('Se ejecuta la condición del tercer if')

print('La ejecución continúa')

if my_condition ==10 :  #Acá le estamos asigando lo que debe de evaluar para el True o False.
    print('Se ejecuta la condición del cuarto if') #Acá pasa ya que la condición cumple la cual si da el resultado de 5*2=10

print('La ejecución continúa')

if my_condition >=10 :  
    print('Se ejecuta la condición del quinto if')

print('La ejecución continúa')

if my_condition <10 :  
    print('Se ejecuta la condición del sexto if')

print('La ejecución continúa')

#2.-HACER ALGO UNICAMENTE CUANDO LA CONDICIÓN NO SE CUMPLE:

if my_condition >10 :  
    print('Es mayor que 10') #Solo se imprime si cumple el if -> Esto lo queremos imprimir únicamente cuando no que sea menor o igual -> 9 y 10 no pasa pero 11 si
else: # -> 'Si no' = Si la condición de arriba se cumple no pasa acá pero si no la cumple entonces si entra al else para dar una respuesta a la pregunta. Caso por defecto.
    print('Es menor o igual que 10') #Si no es mayor debemos de imprimir que es menor o igual

print('La ejecución continúa') #Está línea de imprimr siempre

#3.-CUMPLIR DOS CONDICIONES:
if my_condition >10 and my_condition < 20:  #Evalúa que el resultado de la operación de la variable cumpla con el rango de la condición
    print('Es mayor que 10 y menor que 20') 
else: 
    print('Es menor o igual que 10 o mayor o igual a 20') 

print('La ejecución continúa')


#4.-ELIF:
print('Cuarto ejemplo:')

if my_condition >10 and my_condition < 20: #Las condiciones van en jerarquía de orden. ->Si queremos empezar una ejecución sí o sí debe de empezar con if.
    print('Es mayor que 10 y menor que 20')
elif my_condition == 25: #Necesita de una condición por lo tanto no es lo mismo que el else que es por defecto al no cumplir entra.
    print('Es igual a 25') #Si no se cumple la primer condición entonces aplicará está segunda para comprobación si no se cumple avanza al else pero si se cumple ya no entra al else ya que esta es por defecto para dar una respuesta a la pregunta.
else: 
    print('Es menor o igual que 10 o mayor o igual a 20 o distinto de 25') 

print('La ejecución continúa')


print('Ejemplo de vacíos: ->')
#5.-STRING VACIÓ:
my_string_vacio = '' #Si tenemos un string vacío nos un False por lo tanto no se cumple y no pasa.

if my_string_vacio: #Nos comprueba que está vacía
    print('Mi cadena de texto es vacía1') 

#5.1.-Función de operador de negación:
if not my_string_vacio: #Estamos negando que nuestra cadena no sea vacía entonces lo es. -> Estamos indicando que no está vacía aunque lo está entonces es True.
    print('Mi cadena de texto es vacía2-negación')

if my_string_vacio == 'Mi cadena de textoooooooo': #No pasa ya que el valor definido en la variable que evaluamos es vacía por lo tanto es false
    print('Mi cadena de texto es vacía2')



print('Ejemplo con texto/dato: ->')
#6.-STRING CON DATO:
my_string_dato = 'Mi cade de texto' #Acá ya le asigamos valor

if my_string_dato: #Nos comprueba que está vacía
    print('Mi cadena de texto no es vacía1')



if my_string_dato == 'Mi cade de textooooooooooooooo2': #No pasa ya que la variable definida no tiene todos estos caractéres.
    print('Estas cadenas de texto coninciden')

#Todos los operadores lógicos se pueden concatenar