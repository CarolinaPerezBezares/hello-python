# DICTIONARIES:
#Guarda elementos en forma clave-valor.

#1.-DEFINICIÓN DE DICTS/DICTIONARIES:
my_dict = dict() #Definimos/igualamos la variable con la función 
my_other_dict = {} #Recordar que al poner solo las llaves vacias estamos definiendo la función de dict() pero si al definir una función e igualarla con llaves pero con un valor dentro
#entonces estamos definiendo/llamando a la función de sets().
print(type(my_dict))
print(type(my_other_dict))

#2.-PECULIARIDAD DE LOS DICTIONARIES/DICT:
#2.1.-Diferencia entre set() y dict():Se aguapa por pares -> Relación clave-valor
my_other_dict = {'Nombre': 'Carolina', 'Apellido': 'Bezares', 'Edad':23, 1: 'Python'} #Los datos se agrupan por pares de valores ya que hay una relación clave-valor.
#La clave va al inicio de cada par de datos la cual va acompañada de un valor, ejemplo: CLAVE-'Nombre': VALOR-'Carolina' a los cuales les debemos de definir un valor.

my_dict = { #Tipo de dato clave valor pasando un dato/función más
    'Nombre': 'Carolina', 
    'Apellido': 'Bezares', 
    'Edad':23, 
    'Lenguajes': {'Python', 'Swift', 'Kotlin'}, #Dentro del dict() al valor le pasamos como parametro el tipo de dato set()
    #Si busco la clave 'Lenguajes' de manera inmediata accedemos al set() con los lenguajes guardados y así sucesivamente con las demas claves.
    1: 1.57
    }


print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

#3.-PECULIARIDAD MAYOR DE UN DICCIONARIO: Facilidad de acceder a un elemento.
print(my_dict['Nombre']) #Recuerda que con los corchetes entramos/accedemos a las funciones en este caso el diccionario.

#4.-ACTUALIZACIÓN DE CLAVES:
#Igualamos la variable con el nuevo valor pero también accedemos al valor/clave a la que queremos actualizar
my_dict['Nombre'] = 'Pedro'
print(my_dict['Nombre'])

print(my_dict[1]) #Dependiendo la busqueda que realizamos representamos su valor con lo que le corresponde

#5.-AGREGAR UN NUEVO CAMPO/VALOR AL DICTIONARIES:
my_dict['Calle'] = 'Calle Carolina'
print(my_dict)

#6.-ELIMINAR UN ELEMTO EN NUESTRO DICTIONARIE: DEL
del my_dict['Calle'] #Anteriormente utilzamos del para eliminar toda existencia de la función y variable si colocamos del my_dict pero en este caso solo
#requerimos eliminar un elemento de un dict() la cual el utilizamos el del pero accediendo a la clave que queremos eliminar lo cual es con 'del my_dict['Calle'].
print(my_dict) #Algo eliminado con del no se puede recuperar.

#7.-COMPROBACIÓN DE DATOS EN EL DICT:
#La función de dict() busca el dato por medio de la clave no del valor, siempre que queramos acceder o buscar debe de ser por medio de la clave.
print('Bezares' in my_dict) #Para comprobación de si está o no se hace de la misma que en los set() y arroja un True or False
print('Apellido' in my_dict)
print(my_dict['Apellido']) #De está manera si accedemos para obtener el valor que hay dentro de la clave.

#8.-ALGUNAS OPERACIONES QUE SE PUEDEN REALIZAR EN LOS DICT:
print(my_dict.items()) #Tenemos un listado con cada uno de los items.-Los agrupa y devide pero sigue mostrando todos las claves son sus valores.
print(my_dict.keys()) #Solo nos retorna un listado del formato keys/claves sin los valores pero de manera de una lista porque los retorna y agupa con []
print(my_dict.values()) #Nos retorna todos los valores/values del dict().
#8.1.-Creación de un nuevo dict() pero sin valores, o sea lo creamos y después le podemos añadir los valores
#Creamos la nueva variable en la que irá asigando el nuevo dict() e igualamos haciendo la llamada para crear un nuevo dict() sin valores.

'''
#my_new_dict = my_other_dict.fromkeys(('Nombre', 1, 'Piso'))#Ya depués podemos empezar a crearlo/llenarlo.
#Tenemos un dict() que no nos conserva los datos y los tenemos desde cero.
#-print(my_new_dict) #No necesariamente estamos creando un diccionario en base a ese -> my_other_dict.
#8.2.-Crear realmente un nuevo diccionario con una operación genérica -> dict
my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))
print(my_new_dict2) #Se recomienda para mejor uso crear un dict() como se mostro al inicio e ir añadiendo los valores.
#Esta manera no es muy recomendable ya que cuando queramos acceder al campo no podremos ya que no le hemos seteado aún el valor por eso nos dará un 'None'
'''

#9.-DICCIONARIO DESDE UNA LISTA CON FROMKEYS:
my_list = ['Nombre', 1, 'Piso']

my_new_dict = dict.fromkeys((my_list)) #Hemos creado una lista
print(my_new_dict)

my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))
print((my_new_dict))

my_new_dict = dict.fromkeys((my_dict)) #Le pasaremos un dict() completo - Hemos creado un nuevo diccionario que va reaprovechar todas las claves y después le metemos los datos.
print((my_new_dict)) #Acá si tiene sentido crear un dict con fromkyes
#Creo un diccionario pero solamente tomo las claves y los valores estan vacíos

#10.-ÚLTIMO EJEMPLO:
my_new_dict = dict.fromkeys(my_dict, ('Carolina', 'Bezares')) #Estamos indicando lo que meteremos para cada elemento ya que no tenemos una correlación.
print((my_new_dict))

#11.-TRANSFORMAR DICT A LIST
print(list(my_new_dict)) #Al transformar a lista nos trae las claves sin los valores.

#12.-TUPPLA:
print(tuple(my_new_dict))
#13.-SET:
print(set(my_new_dict))

#14.-VALUES:
#Tenemos un diccionario de valores.
#Si Para tener un valor debemos de transformarlo en lista.
my_values = my_new_dict.values()
print(type(my_values))
#Si accedemos a una lista nos creara una lista de valores
print(my_new_dict.values())
print(list(my_new_dict.values()))