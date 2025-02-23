#SETS:
#Guarda elementos que no esten repetidos y es desordenado.

#Un sets de base tiene un array en cambio una lista de base tenía un array pero en Python no tenemos array como tal si no listas directamente
#Los sets serán muy parecidos a las list() y a las tuple() pero es algo muy diferente.

#1.-DEFINICIÓN DE SETS:
#Definimos/creamos una variable a la cual le añadiremos la palabra reservada set()
#Las palabras reservadas son funciones que se van a construir por eso tiene los paréntesis a los cuales le añadiremos un valor.

my_set = set()
my_other_set = {} #Los set también se definen con llaves PERO al definirlo vacío no es un set es un diccionario/dict, no es como en las listas
#o tuplas al definirlo vacíos con '()' y '[]' ya son tomados como sus respectivas funciones.
#Los sets tienen que tener datos para poder definirse como set().
print(type(my_set))
print(type(my_other_set)) #Acá nos indica que efectivamente al estarlo definiendolo vacío es tipo dict

my_other_set = {'Carolina', 'Bezares', 23} #Al colocarle datos a las llaves ya estámos indicando/definiéndolo que es un set()
print(type(my_other_set)) #Acá nos indica el tipo de dato que es set()

#2.-ALGUNAS OPERACIONES QUE PODEMOS HACER CON LOS SETS:
print(len(my_other_set))#En set() podemos utilizar la operación a nivel sistema que es len() abreviación de length/longitud.
#Nos indica la cantidad de elementos/datos que tenemos en len().

#4.-CARACTEÍSTICAS DE LOS SETS: 
#4.1.-Acá estamos AÑADIENDO un nuevo dato al set().
#4.1.1.-Primer característica de los set() ->Es desordenado!.
my_other_set.add('CarolinaBezares')
print(my_other_set) #Los imprime de manera desordenada pero porque los set() no guarda los datos de manera ordenada, por lo tanto esta es la primer diferencia
#de los set() con los listados e indica que el set() no es un listado ya que los listados son ordenados.
#Por lo tanto es imposible intentar acceder a los elemtos como lo hacíamos en las list() ya que no hay un control absoluto en cada uno de los elementos.

#4.2.-Segunda característica los set() no admite elementos/datos repetidos!.
my_other_set.add('Carolina Bezares') #Acá estamos añadiendo nuevamente un nuevo elemento al set()
print(my_other_set) #Al imprimir podemos ver que solamente imprime/muestra un solo elemento de 'MauroDev' aunque anteriormente se añadio un elemento con el mismo nombre.
#Esto se debe a que los set() no admiten datos/elementos repetidos.
#Para permitir que no acepte/exista repetidos es más facíl a la estructura set() no guardar ese rato.


#5.-COMPROBACIÓN DE LA EXISTENCIA DE UN ELEMENTO DENTRO DEL SET:
#Nos da un True or False como resultado.
print('Carolina' in my_other_set) #Elemento que estamos pidiendi comprobar si está in/en el set().
print('Caro' in my_other_set)

#6.-ELIMINACIÓN DE DATOS:
my_other_set.remove('Carolina')
print(my_other_set)

#7.-LIMPIEZA DE ELEMENTOS DE LOS SETS-NO ELIMINA EL CONSTRUCTOR/VARIABLE DEL SET:
my_other_set.clear()
print(my_other_set) #Acá nos muestra que tenemos en existencia una instancia de un set() aun sin definir y vacío
print(len(my_other_set)) #Nos muestra la longitud del set() que tenemos la cual es 0 ya que el set se encuentra aun sin definir por lo tanto sin datos.


#8.-BORRAR SETS-DEL:
#del es una palabra reservada del sistema por lo tanto no está asociado a los set()
#Para acceder a las operaciones propios de un objeto es con un punto'.' -> solamente la variable seguida de un punto, ejemplo: my_other_set.clear().
del my_other_set #Eliminación completa del set()
#print(my_other_set) Al ya estar eliminido el objeto de raíz/existencia el print() al llamar la variable no puede ya que está junto con sus datos no existe.
#NameError: name 'My other set' is not defined.


#9.-TRANSFORMACIÓN DE UN SET A UNA LISTA:
#Volvimos a crear la variable y sus elementos ya que anteriormente la limpiamos y también borramos.
my_set = {'Carolina', 'Bezares', 24}
my_list = list(my_set)
print(my_list) #Al pasarlo a una lista ya tenemos datos/elementos ordenados, por lo tanto ya podemos acceder a los elementos.
print(my_list[0]) #Acá estamos accediendo a la posición de los elementos de a list() que contiene los datos ordenados de cuando era un set()
#No se recomienda este tipo de transformaciones ya que al volver a transformarlo como set() inmediatamente perderemos el orden de los datos.

#10.-UNIÓN DE DOS SETS:
#Volvemos a definir nuestro set()
my_other_set = {'Kotlin', 'Swift', 'Python'}
#Creamos una nueva variable en la cual se guardará/almacenara la suma de ambos set()
#Accedemos a nuestro primer set junto con llamar la operación union() a la cual pasaremos como parametro/valor el siguiente set()
my_new_set = my_set.union(my_other_set) #Para poder unir/sumar set() utilizamos la operación propia del objeto de set() la cual es union.
print(my_new_set)
#Podemos añadir union() cuantas veces queramos con los mismos set() pero siempre imprimira/mostrara los mismos datos que al incio ya que en set()
#no acepta números repetidos por lo tanto como ejemplo siempre tendremos los mismos 5 datos así añadamos los mismos 5 datos 7 veces.
#Pero al añadir nuevos datos dentro del unión de manera inmediata los añadirá ya que no son datos que tengamos por lo tanto no son números repetidos.
#No hay problema si no añadimos por medio de crecación de una variable como anteriormente se muestra ya que con el simple hecho de añadirlo dentro del
#parametro de union() los tomara/guardara para añadirlos al set en unión.
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', 'C#'}))

#11.-OPERACIÓN DIFERRENCE/DIFERENCIA:
#Acá esta buscando y mostrando la diferencia de los datos que hay entre ambos sets que elegimos/pusimos.
#Por lo tanto a my_new_set le estamos quitando los elementos que hay en my_set por lo tanto el resultado que muestra es los elementos que hay en my_set.
#No aparecen los datos que añadimos en el parametro de union() dentro del print() ya que los datos como tal están en el union() más no en el set() por lo tanto no está definido como elemento dentro
#de la variable my_new_set.-Esto quiere decir que esos datos de la ejecución del print() en el union() no están almacenados en una variable.
print(my_new_set.difference(my_set))


#3.-FORMA DE ACCEDER A LOS ELEMENTOS: Es imposible intentar acceder a los elemtos como lo hacíamos en las list() ya que no hay un control absoluto en cada uno de los elementos.
#En las list() para poder acceder a los elementos es por medio de los corchetes [] justo a la de la variable y poniendo dentro la posición del elemento al que queremos acceder.
#print(my_other_set[0]) Ejemplo de como podría ser pero en los set() es erroneo.


#CARACTERÍSTICAS DE LAS TUPLAS Y LAS LISTAS QUE SET NO TIENE:
#1.-Admiten repetidos
#2.-Son ordenados al momento de imprimirlos/mostrar los datos.
#3.-list() -> podemos añadir elementos y siempre van al final después de agregarlo.
#4.-tuple() -> ser elementos inmutables.
#5.-list() acceder a un elemento en concreto. también en tupple()
