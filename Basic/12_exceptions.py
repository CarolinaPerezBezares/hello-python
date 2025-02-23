#EXCEPTIONS HANDLING/MANEJO DE ERRORES:

number_one, number_two = 5, 1

number_two = '1'

#1.-ES UNA PALABRA RESERVADA DEL SISTEMA: try

#Es un try except. -> Es un error controlado: La función no pasa pero no se detiene, continua pero sin hacer la operación y lanza el comentario de que se produjo un error.
try:
    print(number_one + number_two)
    print('No se ha producido error')
except: #Se ejecuta si se produce una excepción. -> except: Va siempre, si o si. ->
    print('Se ha producido un error')


#Es un try except else.
try:
    print(number_one + number_two)
    print('No se ha producido error')
except:
    print('Se ha producido un error')
else: #Se ejecuta si no se produce una excepción. -> except: Es opcional utilizarlo.
    print('La ejecución continúa correctamente')


#Es un try excep else finally.
try:
    print(number_one + number_two)
    print('No se ha producido error')
except:
    print('Se ha producido un error')
else: #Se ejecuta si no se produce una excepción. -> except: Es opcional utilizarlo.
    print('La ejecución continúa correctamente')
finally: #Se ejecuta siempre pase lo que pase. -> finally: Es opcional utilizarlo.
    print('La ejecución continá')

#Exceptions por tipo.
try:
    print(number_one + number_two)
    print('No se ha producido error')
except ValueError: 
    print('Se ha producido un ValuError')
except TypeError: #Este bloque except solamente se ejecuta si se produce 'TypeError' si no es así pasa a la siguiente y lo mismo -> Es un error controlado definido pero hay más tipos.
    print('Se ha producido un TypeError')


#Captura de la infomación de la excepción:
try:
    print(number_one + number_two)
    print('No se ha producido error')
except ValueError as error: #Capturar errores as 'error' es la variable que captura la información. -> Este except es tipo concreta
    print(error) #Tenemos un objeto con valor. -> error: Guarda el error que se ejecuta.
except Exception as exception: # Exception es genérica. -> Sea lo que sea el error se controla
    print(exception)

