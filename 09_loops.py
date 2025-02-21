#LOOPS -> Funciona con elementos iterables:Son aquellos que podemos recorrer usando un ciclo
#Nos sirve para pasar por el mismo código varías veces.

#Tenemos diferentes tipos de estos: While,for, doWhile


#1.-PRIMER TIPO: While
#Hay que pasarle una condición: Mientras sea verdadero has algo

my_condition = 0

while my_condition < 10: #El while hace que se repita varías veces en función de una condición.
    my_condition += 2 #Tenemos que hacer que nuestra condición/valor sea diferente al dar una vuelta para que en algún punto tenga un final si no está será infinito.
    print(my_condition) #Al valor de 0 le estamos pidiendo que se le sume este valor y dará las vueltas necesarias hasta cumplir la primer condición.
else: #Cuando no cumpla pasa a dar una respuestan. -> "Es opcional utilizarlo".
    print('Mi condición es mayor o igual que 10')

print('La ejecución continúa')

#1.1.-WHILE IF, BREAK
while my_condition <20:
    my_condition += 1
    if my_condition == 15:
        #print('Mi condición es 15') #Este print es para el ejemplo sin break.
        print('Se detiene la ejecución') #Se da si cumple la primer ejecución pero no la segunda entonces en lugar de seguir avanzando lo paramos.
        break #Se da por tener una condición muy en concreto que nos obliga a detener la ejecución.
    
    print(my_condition)


print('La ejecución continá')

#2.-SEGUNDO TIPO: For
#Itera un listado de elementos, de igual manera tiene que cumplir una condición.

#Primero definimos una lista.
my_list = [35, 24, 62, 52, 30, 30, 17] #Elementos iterables -> Cualquier estructura que tenga la capacidad de alamacenar elementos es iterable.

for element in my_list: #En el for se va repetir tantas veces como elementos tengamos iterables. -> En cada vuelta accede a cada uno de los elementos.
    print(element)

#Primero definimos una tuple.
my_tuple = (23, 1.57, 'Carolina', 'Bezares', 'Carolina')

for element in my_tuple:
    print(element)

#Primero definimos un set.
my_set = {'Carolina', 'Bezares', 23}

for element in my_set:
    print(element)

#Primero definimos una dict.
my_dict = {'Nombre': 'Carolina', 'Apellido': 'Bezares', 'Edad':23, 1: 'Python'}

#De igual que en while también podemos utilizar con el for un if, break y else:
for element in my_dict: #Si utilizamos un for con un dict() imprime las claves/keys no el formato clave-valor. -> Si queremos imprimir el valor del dict() es:'for element in my_dict.values()'
    print(element)
    if element == 'Edad':
        break #Condicionamos que se pare al llegar a 'Edad'. -> Rompemos el bucle y no pasa lo que este por delante.
else: #También se puede utilizar acá -> Al terminar el bucle entra, acaba e imprime.
    print('El bucle for para mi diccionario ha finalizado') 

print('La ejecución continá')

#2.1.-Continue: También se puede utilizar está palabra reservada en el while.
for element in my_dict: 
    print(element)
    if element == 'Edad':
        continue #No deja que la vuelta que cumpla la condición ejecute la vuelta completa pero te envía al incio para que puedas seguir con las vueltas restantes. ->Indica que si llega a cumplir la condición prosiga con el bucle pero sin completar esa vuelta.
    print('Se ejecuta')
else: 
    print('El bucle for para mi diccionario ha finalizado') 