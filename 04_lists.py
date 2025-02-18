#LIS/LISTAS:
#Se refiere a que ya estamos hablando de una estrauctura para estructuras los datos.
#array, arreglos, pilas: estás son las listas de nivel básico de programación pero en Python las listas son lo siguiente:
#Son los arreglos pero no como tal es eso ya que los arreglos tienen ciertas limitaciones en operaciones y en las listas se puede hacer un poco más.
#Listas: operaciones más complejas e inteligentes-Nos suelen dar operaciones de inserción, recolocación, ordenación a la hora de contar tamaños, etc.

#Se dice que todo en Python es un objeto porque es un lenguaje orientado a objeros y este tipo de lenguajes suelen extender todos sus tipos de datos de
#algo básico que puede ser un objeto.-algo que tangiblemente podemos manejar.

#Array, arreglo y lista: Será lo mismo para nosotros porque la lista será como un super conjunto de un arreglo.


#1.-LISTA: Si tenemos una lista significa que podemos acceder a los elementos por separado.
#Es una forma de agrupar datos siguindo un orden/lista
#1.0-Tipos de definición de uso de una lista:
my_list = list()
my_other_list = [] #Esto también es una lista

print(len(my_list))#Imprime 0 elementos ya que al llamar la lista hay cero elemtos ya que está vacio.
#Para contar se utiliza el len().
#1.1-Guardar tipos de datos igual:
my_list = [35, 24, 62, 52, 30, 30, 17]#Añadimos un array de elemtos:de lo que nosotros queramos-al ser Python un lenguaje de tipado dinámico podemos guardar lo que queramos.
#Nota: No olvidar que al definir una variable le estamos asignando datos/valores
#Podemos guardar el mismo valor mas de una vez en la lista y no hay problema.
print(my_list)#Acá imprime los elementos que tenemos en la lista
#1.2-Longitud de los datos:
#No tenemos los elemtos solo para tener la longitud de ellos, si no para poder acceder a ellos.
print(len(my_list))#Acá imprimimo lo que calcúlamos de la longitud de la lista.
#1.3-Mezclar los datos:
my_other_list = [35, 1.77, 'Brais', 'Moure']#No da problemas e indica que no hace falta que en la lista estemos guardando siempre el mismo tipo de dato
#1.4-Saber tipos de datos:
print(type(my_other_list))#type() nos sirve para ayudar a saber que tipo de dato tenemos
print(type(my_list))

#2-ACCEDER A LOS VALORES DE LA LISTA:
#Al colocar el número/posición estamos pidiendo acceder/mostrar lo que se ha asiganado.
#Recuerda que empieza desde la posición cero al contar o asignar lugares.
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])#Empieza de atrás hacía adelante
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count('Brais'))#Count() vació marca error por lo tanto debemos de ayudarlo pasando un parametro
print(my_list.count(30))#Para contar elementos dentro de la propia lista se utiliza el count()
#print(my_other_list[4]) IndexError: Se debe a que esa posición no existe ya que no hay un valor existente que ocupe el lugar.
#print(my_other_list[-5]) IndexError

#2.1-Definir varias variables en una sola línea y restructurales de alguna forma:
#No es una manera muy recomendable al tener varios datos ya que nos podemos confundir al desempaquetar.
age, height, name, surname = my_other_list #Lo estamos igualando a my_other_list
#Acá desempaquetamos todos los elementos de la lista.
print(name) #Hacemos un prin de cualquiera

#2.2- Sumar listas/Concatenar listas:
print(my_list + my_other_list)
#print(my_list - my_other_list)#Error de aplicación


#4-LISTA MUTABLE:
#Empezar a trabajar con los elementos de la lista:
#4.1-Añadir un nuevo elemento a la lista:
my_other_list.append('MauroDev') #Añadimos un nuevo elemento a la lista ya definida anteriormente.
#Un append() añade un nuevo elemento/inserta al final de la lista
print(my_other_list)
#4.2-Insertar datos a la lista:
my_other_list.insert(1, 'Rojo')#Un insert() es que en la posición que indicas inserta el valor que estás indicando/asigando y se corre la posición 
#del valor que antes ocupaba ese lugar, en este caso 1.77 se corre a la posición 2.
print(my_other_list)#Impresión del cambio de valores

#8.-CAMBIAR EL VALOR/MODIFICAR UN DATO EXISTENTE:
my_other_list[1] = 'Azul' #Acá estamos accediendo al valor que en este caso es 1 y lo estamos igualando/modificando/cambiando a 'Azul'.
#Anteriormente el valor que estaba asigando en 1 era 'Rojo' pero ahora lo hemos modificado a 'Azul'
print(my_other_list)

#4.3-Eliminar un valor en la lista con remove()
#remove() es para eliminar un elemento que conocemos y sabemos que esta dentro de la lista.
my_other_list.remove('Azul')#Acá estamos indicando el valor que queremos eliminar
print(my_other_list)

my_list.remove(30) #Indicamos que no queremos el valor int 30
print(my_list)

#5.-COLAS: Operaciones que son estructuras que se generan a través de de arrays y arreglos.
#Esta es la forma de eliminar un elemento en un lugar concreto pero retornando ese elemento.
#pop() es la manera de eliminar ese elemento pero nos quedamos con el porque queremos saber el valor del que estamos eliminando.
my_list.pop() #Elimina el último elemento por defecto pero se puede utilizar a libre criterío
#pop() elimina el valor pero por si lo necesitamos nos esta devolviendo el valor que hemos desapilado
print(my_list)

print(my_list.pop()) #En esta impresión muestra la explicación anterior sobre el retorno de valor, acá muestra/imprime el número retornado.
print(my_list)

print(my_list.pop(2)) #Acá estamos aplicando el libre criterío ya que estamos asigando eliminar el número que se encuentra en la posición #2 de la lista.
print(my_list) #Recueda las posiciones empiezan desde el número 0

my_pop_element = my_list.pop(2) #Acá creamos una variable para asi poder guardar el elemento desapilado ya que antes no se estaba guardado solo desapilando.
print(my_pop_element)

#6.-ELIMINAR UN ELEMENTO DE LA LISTA:
#del elimina por indice indicado
#Eliminamos sin retornar nada porque ya no lo queríamos
del my_list [1]#Acá solo estamos indicando que no queremos el valor que se encuentra en el indice/posición #2.
print(my_list) 

#9.-COPIAR LISTAS:
my_new_list = my_list.copy() #Acá hemos llamado a la función de copy y lo hemos asignado a una nueva variable en la cual estará el valor.


#7.-CLEAR:
my_list.clear() #Eliminamos todo el contenido de la lista, queda totalmente vacía
print(my_list)
print(my_new_list) #Acá estamos imprimiendo la copia de la lista la cual debería de estar llena ya que se copio antes de realizar el clear()
#Esto se debe a que la variable y función se asigno antes de pasar por esta variable y función de clear().

#10.-FUNCIÓN DE REVERSA:
my_new_list.reverse() #Primero debemos e ejecutar el reverse()
#La función de reverse() es darle vuelta a la lista, o sea que los valores del final sea el inicio y lo valores del inicio el final
print(my_new_list)

#11.-ORDENA:
#Indicamos criteríos para ordenar
my_new_list.sort()#Sin importar el tipo de dato que tengas sort() se encargara de buscarles un orden.
#El punter sobre la función nos proporciona la información la cual nos indica que nos retorna un 'None' porque debemos de ejecutarlo primero
#para después empezarlo a trabajar.
print(my_new_list)

#REBANADAS:HACER SUBLISTAS
print(my_new_list[1:2]) #Acá estamos indicando que queremos el o los elemtos que se encuentran en los rangos entre 1 y 2, nos da el resultado
#en una sublista pero imprime la lista anterior/original y debajo de ella imprime la nueva lista con el dato indicado
#print(my_new_list[1:3]) #Acá estamos haciendo exactamente lo mismo que en la anterior.


#3-TIPOS DINÁMICOS:
my_list = 'Hola Python'#Estamos cambiando los valores asignados anteriormente a la lista y ahora ya no es una lista es un string=str().
print(my_list)
print(type(my_list))

#Hemos cambiado el tipo de dato ya que es un tipado dinámico y así funciona el lenguaje.-Esto nos permite trabajar con diferentes tipos de datos
#a lo largo de nuestro programa y los podemos cambiar.
#Nota: Para tener una constante quizás una manera es poner el nombre de la variable es mayúscula pero esto no asegura nada que alguien más venga y le cambie el valor asigando.
#Ejemplo:MY:CONSTANT = 'name'