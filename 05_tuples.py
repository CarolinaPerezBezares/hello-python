#TUPLES/TUPLAS:
#Guarda elementos pero no se pueden retocar. -> son inmutables.

#Las tuplas() son inmutables y si las utilizamos es porque queremos trabajar con valores constantes.
#Si queremos trabajar con valores mutables entonces trabajamos con list()

#1.-CÓMO DEFINIR UNA TUPLA?
#La podemos definir con su nombre reservado tuple().
#Es el constructor da la/s tupla.
my_tuple = tuple() #Manera 1
my_other_tuple = () #Manera 2
#No hay que confundirse de que solo las tuplas() van con parentesis ya que un constructor también lleva parentesís '()'
#Aunque a nivel sintáctico si no le metemos el constructor de clase tendríamos lista[] y tupla().

#2.-EJEMPLO DE UNA TUPLA:
#Igualamos la tupla con los datos siguientes:
my_tuple = (23, 1.57, 'Carolina', 'Bezares', 'Carolina')
my_other_tuple = (35, 60 , 30)

print(my_tuple)
print(type(my_tuple))

#3.-POSICIONARNOS EN EL LUGAR DE UN VALOR DE LA TUPLA
print(my_tuple[0]) #Nos pocisionamos en el lugar del elemento.
print(my_tuple[-1]) #La función de pocisionarse con un número negativo es para que empieza de manera contraria es decir que el final sea el inicio,
#pero ya no empieza de cero empieza a contar desde la primer posición como -1 tomando este el lugar del 0.
#3.seguimos con las pruebas:
#print(my_tuple[4]) Nos da un 'IndexError'
#print(my_tuple[-6]) Nos da un 'IndexError'

#4.-INSERTAR VALORES Y REALIZAR OPERACIONES:
#Las unicas dos operaciones que tenemos a realizar en las tuplas() son count() e index(), lo cual es una de las diferencias entre las listas y tupplas.
print(my_tuple.count('Carolina')) #4.1.-El count() tiene la misma función como en las listas que se le pasa un valor y revisa/cuenta en la tupla
# para colocar el total de ese valor existente o revisar si existe/hay.

print(my_tuple.index('Bezares')) #4.2.-La función de index() es marcar el indice/posición del valor que hemos mencionado, en este caso 'Moure' 
#que nos indica que se encuentra en la posición 3 empezando de 0 a 3.
print(my_tuple.index('Carolina'))

'''
5.-LAS TUPLAS SON INMUTABLES:
En las listas los datos de ellas son dinamicos pero en las tuplas no ya que los valores son inmutables, lo cual quiere decir que podemos guardar datos en ellos
pero tenemos un conjunto de valores cerrados e inicializados.-Una vez definido los datos en la tuppla() ya no los podemos modificar.

my_tuple[1] = 1.80 Esto es un error al querer aplicarlo en una tuppla()->'tuple' object does not support item assignment, pero en listas[] es correcto.
'''

#6.-SUMAR TUPLAS:Se pueden sumar
#print(my_tuple + my_other_tuple) Es una forma de prueba/comprobación para ver si permite sumar diferentes tuplas().

my_sum_tuple = my_tuple + my_other_tuple #Creamos una variable en la que estará el conjunto de ambas tupplas.
#En esta variable le asiganamos como valor la operación de la suma de las tuplas dando el resultado el conjunto de ambas.
print(my_sum_tuple)

#7.-ENTRAR A LAS TUPLAS Y POSICIONARNOS:
print(my_sum_tuple[3:6]) #Entramos y buscamos para posicionarnos en los elemtos que nos está indicando los cuales son el valor de la posición 3 hasta el valor de la posició 6
#junto con los valores que se encuentran dentro de ese rango entre 3 y 6.
#Es como si empezaramos en el indice 3 pero en realidad empezamos en el elemnto 3.


#8.-TRANSFORMAR TUPPLA PARA QUE YA NO SEA TUPPLA:
#Si queremos trabajar con valores mutables entonces trabajamos con list()
my_tuple = list(my_tuple)#Acá estamos diciendo que nuestra tupla sea una lista->estamos reasignando.
print(my_tuple)
print(type(my_tuple))

#8.1-Cambiamos nuestra tuppla() a una list() porque en realidad queríamos cambiar un valor de la tupla(). ->Este se hace en un caso muy necesario porque no se recomienda cambiar una tuppla.
my_tuple[4] = 'CarolinaBezares' #Estamos insertando un nuevo valor y posición a la tuppla()/list() -> La posición 4 no existía. 
print(my_tuple)
my_tuple.insert(1, 'Azul') #Estamos diciendo que ahora en la posición 1 queremos que tenga otro valor 'Azul' ->Acá estamos recorriendo el valor a la siguient posición.
print(my_tuple)

#8.2-Ahora volvemos a cambiar/transformar nuestra tupla a tupla:
my_tuple = tuple(my_tuple) #Acá estamos reasignando nuestra list() a tupla()
print(my_tuple)
print(type(my_tuple))

'''
#9.-BORRAR TUPLAS:del
del my_tuple #Esta variable ya no está definida porque la hemos borrado con todo y su contenido por lo tanto no se puede ejecutar la impresión porque la variable que queremos que imprima/muestre
#no existe y por lo tanto no hay ni siquiera un contenido el cual hay que mostrar
#No es como un clear() que solo borra el contenido de la variable mas no a la variable,
#del es una palabra reservada del sistema por lo tanto realiza de manera concreta la tarea que la asigamos y del no es parte/típico de las tuplas ya que como es del sistema lo podemos utilizar
#en cualquier tipo de variable que utilizemos y será propio de cada una ya que no es especificmante de una.
print(my_tuple)#Es un error debido a que la variable ya no existe por lo tanto no hay nada para llamar/mostrar. -> NameError: name 'my_tupla' is not defined.

'''

#En las tuplas al utilizar del no podemos hacer lo mismo que en las listas al querer eliminar definitivamente un elemento de la lista ya que como es
#inmutable tampoco podemos eliminar solamente un elemento de las tuplas, es eliminar toda la tupla o nada
#del my_tupla[2] Ejemplo que como eliminamos en list() aplicandolo en tuplas() pero esto es incorrecto/error. ->TypeError: 'tuple' object doesn't support item deletion.
