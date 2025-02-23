#FUCTIONS:

#Una función va intentar resolver un problema muy concreto ya que nosotros le indicaremos  el problema.
#Evita errores -> Todo el código que se va resolver estará en un lugar.
#Concatenar: Unir o enlazar dos o más cosas.


#1.-DEFINICIÓN DE FUNCIONES: Se crea con la palabra reserva def
#Las funciones no sirven solo para llamarla y que ejecuten el código -> También puede devolver y recibir código, ya no solo desencadena.

def my_function ():
    print('Esto es una función')

my_function() #Acá estoy llamando a la función. -> Trae lo que contiene y lo muestra.

#2.-PARAMETROS:
#Tenemos dos tipo de parametro: De entrada -> Son los que reciben y necesitan las funciones para ejecutarse y De salida -> Los que la función devuelven.

#Acá el tipado no funciona porque no podemos forzar un tipo de dato en concreto-> int etc., pero podríamos ponerlo para que sea predecible para el programador..
#Acá sumaremos dos valores.
def sum_two_values (first_value: int, second_value): #Estos son los parametros a los cuales les añadiremos un valor. -> Parametros de entrada
    print(first_value + second_value) #Podemos implementan una condición u operación con los parametros.
#Esta función se ejecuta sin retornar un valor.

sum_two_values(5,7) #Añadimos los valores de los parametros  con los cuales se aplicará la condición/operación.
sum_two_values(54754,71231) #La variable va tomar el valor del tipo de dato que le metamos.
sum_two_values('5','7') #Las cadenas de texto se concatenan al tener un '+'. -> Está en los parametros de la función
sum_two_values(1.4,5.2)


#RETORNAR PARAMETROS:
#Haremos que pasen los parametros pero no dejaremos que parte de lo que hagamos en la función se quede dentro de ella -> Hacer algo concreto y retornar.


def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value, second_value
    #return first_value + second_value #Va con la operación que queremos retornar. -> Nuestra función ya es capaz de asignarle el resultado a una variable.
    return my_sum

my_result = sum_two_values_with_return(10, 5) #Guardamos en una variable nuestro resultado que retorna/devuelve un valor. -> No está vacía ya que retorna algo
print(my_result) #Podemos imprimir el valor con la variable de almacenamiento. -> De igual manera podemos pasar e imprimir directamente la función sin tenerla guardada: 'print(sum_two_values_with_return(10, 5))' pero no es funcional.


#PARAMETROS POR DEFECTO
def print_name_with_default(name, surname, alias = 'Sin alias'): #Definimos un valor por defecto. -> No importa si lo dejan vacío.
    print(f'{name} {surname} {alias}') #f -> Formateo: Accedemos a los valores '{name-Carolina}{surname-Bezares}' para convertir en una cadena de texto que se va concatenar los valores que llegan como parametro.

#print_name('Carolina''Bezares') #Sin la f solo imprime la cadena de texto '{name} {surname}' pero no los valores ya que no accede a ellos. -> Estamos imprimiendo sin orden.
#print_name(surname = 'Carolina', name = 'Bezares') # Estamos reordenando. -> Llamamos a los parametros quienes tienen el orden.
print_name_with_default('Carolina', 'Bezares')
print_name_with_default('Carolina', 'Bezares', 'CarolinBezares')


def print_upper_text(*texts): #El * nos permite pasar más de un solo texto. -> Nos permite pasar cuantos parametros queremos.
    for text in texts: #Vamos a iterar un texto
        print(text.upper()) #Estamos pasando a mayúscula todos los textos.

print_upper_text('Hola', 'Como estás', 'Adios') #Se vuelen parametros dinámicos. -> Funcipon con parametros arbitrarios: Pasamos parametros separados por ','.
print_upper_text('Hola')
