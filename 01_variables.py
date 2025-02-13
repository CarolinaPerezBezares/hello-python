#VARIABLES: Como su nombre lo indica, quiere decir que al ser una variable puede variar.

#Hay una nomenclatura con el nombre "camel case", que significa ir siguiendo la joroba de un camello
#Esto quiere decir que la primera letra de una palabra se empieza en minuscúla y cada letra de una nueva letra de la palabra va en mayuscula.
#Pero al estar dentro de la misma palabra, pero OJO: en Python esto no está permitido, tiene su propia nomenclatura.
'''
myStringVariable = 'My String variable'
print(myStringVariable)

'''



#NOMENCLATURA DE PYTHON=
#Las variables deben de ir en minúsculas y en snack case: Esto quiere decir con un guión bajo. NO con guiones medios o caracterés especiales.
#Nota: No se recomienda hacer variables tan largas por problemas al recordar el nombre.

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
#Python funciones sobre un interprete, y acá está haciendo un valor de pre-interpretado 
#para que nos vaya diciendo en dónde están los errores.
my_bool_variable = False
print(my_bool_variable)


#CONCATENACIÓN DE CADENAS/VARIABLES EN UN PRINT:
#A print se le pueden pasar varios argumentos, esto es posible ya que se pueden separar por comas.
print(my_string_variable,my_int_variable,my_bool_variable)
#Es para que nosotros podamos pasar diferentes datos que va a realizar/necesitar/tomar dentro de una cadena.
#Ha sido de modificar/tomar el valor de todas las variables y el resultado es la tranformación de tomar todos los
#datos para formar una cadena de texto.

#VARIBALE PARA QUE UTILIZEMOS UNA DE LAS FUNCIONES DEL SISTEMA:
my_int_to_str_variable = str(my_int_variable)#Acá impriminos el str que tiene como parametro el entero que es la variable con el valor:my_int_variable, por lo cual sigue impriendo o teniendo el valor de 5.
print(my_int_to_str_variable)#Acá esta impriendo el 5 que es un número tipo entero pero al ser/estar en un print es una cadena de texto
print(type(my_int_to_str_variable))
#Por qué el print(my_int_to_str_variable) imprime el valor de 5? Facíl, es porque anteriormente al crear la variable le estás asignando o convirtiendo
#un valor el cuál está siendo la variable que contiene el valor del 5 que es my_int_variable, por lo tanto ahora ambas tienen el mismo valor.
#pero ojo al asignarle ese valor con str se transforma a una cadena de texto.
#El último print contiene type(my_int_to_str_variable), lo cual quiere decir que estamos pidiendo que imprima/diga/indique el tipo de función.

#UTILIZANDO UNA DE LAS FUNCIONES DEL SISTEMA:
print(my_string_variable, str(my_int_variable),my_bool_variable)

#Datos de print: El print es capaz de tomar todas las variables y acabar transformandolas a algo que sea posible imprimir por 
#consola, o sea una cadena de texto: print().

print(len(my_int_to_str_variable)) #Da de resultado 1
print(len(my_string_variable)) #Da de resultado 18
#Len es una abreviatura de 'Lenght' que significa longitud por lo tanto la función de 'len()' se encarga de contar
#la cantidad total de los caractéres de las variables pero incluso cuenta incluyendo los espacios que hay.

#LOS print() TAMBIÉN PUEDEN RECIBIR PARAMETROS: 
#También se le conoce como concatenar, no lo olvides y acá es un ejemplo de las muchas concatenaciones que existen.
print(my_string_variable,my_int_variable,my_bool_variable)
print('Este es el valor de mi variable boolean:', my_bool_variable) #Le metemos una cadena de texto ya prefijada/fija
#Ojo:El texto va dentro de las comillas y si quieres poner el valor que va imprimir va una coma para
# dividir/agregar un valor que va fuera de las comillas para que pueda reconocerlas como variables.

#VARIABLES EN UNA SOLA LÍNEA:
name, surname, alias, age = 'Carolina', 'Pérez', 'Caro', 23 #Se pueden mezclas tipos de datos
print('. -Mi nombre es:', name, surname, '. -Mi edad es:', age, '. -Y mi alías es:', alias)
#!No se recomienda utilizar esta sintaxis ya que hace todo más tedioso en cuanto a posibles errores futuros¡.
#Solamente se recomienda al utilizar solo dos valores.

#EJEMPLO DEL USO DEL INPUT:
#Es un teclado en pantalla, lo cual no es tan recomendable ya que solo se puede si son aplicaciones/scripts o algo que ejecuten
#trabjando directamente desde la terminal
'''''
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
'''''
#Termina al colocar el último dato pedido e imprime los datos que se han pedido.

#CAMBIAMOS EL TIPO DE DATO:
name = 35
age = 'Brais'
print(name)
print(age)
#Hay que tener cuidado al asignar valores a las variables ya que Python acepta sin problemas los datos,
#esto puede afectar a un futuro si estamos trabajando en un proyecto más grande y/o con más personas.

#FORZAMOS EL TIP?O:
address: str = 'Mi dirección'
address = 32 #Acá le hemos cambiado el tipo de dato.
print(address)
print(type(address))

