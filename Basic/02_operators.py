#OPERATORS/OPERADORES

#EJEMPLO DE OPERADORES ARITMÉTICOS:

#EJEMPLOS DE ALGUNOS TIPOS
#no se empieza por un print ya que es para ver datos por consola y fue para ver un ejemplo básico de 
#la funcionalidad de los operadores.
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

# "6+10" Sin el print el resultado no se refleja en la consola
#No se esta haciendo absolutamente nada porque no se está almacenando en ninguna variable

#OPERADOR DE MÓDULO: Es que nosotros estemos estableciendo una división y nos diga cuál es el resto
#modulo igual para saber si hay un múltiplu por en medio.-podría ser una manera de calcular
print(10 % 2)
print(10 % 3)

#En Python se realizan operaciones que en otros lenguajes no son tan fáciles de hacer.

#DIVISIÓN:
print(10 / 3) #División normal
print(10 // 3) #Esta división acaba apróximada a un número entero.-aproximar/viene en décimal


#CALCULAR EXPONENTE:
print(2 ** 3)

#CONCATENAR:
#el signo no solo funciona para realizar operaciones ya que también los concatena.
print('Hola' + 'Python')
#acá tomo ambos textos y al sumarlos lo unio quitando el espacio, perooo
print('Hola ' + ' Python ' + 'Qué tal?')
#acá le añadimos espacio al texto en las comillas para que al ejecutar tuvieran los espacios.

#NOTA: No se pueden mezclar los tipos de datos al concatenar
#print('Hola ' +  5) Entero con string.-error

print('Hola ' + str(5)) #Aplicando funciones de sistema 'str()'
#como estamos llamando a la función del sistema str() esta transformando un número/algo
#a un string, por lo tanto al concatenar funciona porque llama a la función del sistema.
#acá forzamos a un dato que no es string se vuelva string-estamos concatenando en este print.

#TODOS LOS SIGNOS SE PUEDEN COMBINAR ENTRE ELLOS:
print(2 ** 3 + 3 -7 / 1 // 4) 

#EJEMPLO DE ALGUNAS FUNCIONES DE LOS OPERADORES:
print('Hola ' * 5)
print('Hola ' * (2 ** 3))

my_float = 2.5 * 2
print('Hola ' * int(my_float)) #acá funciono porque se forzo a cambiar el tipo de dato float() a int().
#Solo son ejemplos de lo que nos permiten hacer los operadores.

#Este es el fin de los ejemplos de los operadores ariméticos.

#EJEMPLO DE OPERADORES COMPARATIVOS:
#Opcional trabajar con fuente firacode-admite ligaduras

print(3 > 4) #Mayor que
print(3 < 4) #Menor que
print(3 >= 4) #Mayor o igual que
print(3 <= 4) #Menor o igual que
print(3 == 4) #Igual
print(3 != 4) #Diferente que o no es igual
print(3 > 4 == 2) #Ejemplo de que pueden mezclar diferentes operadores

#LOS OPERADORES TAMBIÉN SE PUEDEN UTILIZAR CON CADENAS DE TEXTO

print('Hola' > 'Python')
print('Hola' < 'Python')
print('Hola' >= 'Zola') #Comprueba una ordenación alfabética no los caractéres en función por ASCII
#Si queremos comprobar una cadena de texto es de la siguiente manera:
print(len('Hola') >= len('Zola'))
#len() es para calcular una longitud de una cadena de texto, por lo tanto por eso cuenta caractéres.
print('Hola' >= 'Python')
print('Hola' == 'Python')
print('Hola' != 'Python')


#OPERADORES LÓGICOS:
#Nota: La lógica boolena rige toda la programación: (false and false = false), (false and true = false), (false or false = false).

print(3 > 4  and 'Hola' > 'Python') #False and False = False
print(3 > 4  or 'Hola' > 'Python') #False o False = False
print(3 < 4 and 'Hola' < 'Pyhton') #True o True = True
print(3 < 4 or 'Hola' > 'Python') #True or Flase = True
print(3 < 4 or ('Hola' > 'Python' and 4 == 4)) #Acá definimos el orden de prioridad como en calcúlo:parentésis, etc.
#Si no definimos el orden el sistema lo hará conformo su orden de el o por orden de operación(el ordén en que se escribió)
print(not(3 > 4)) #3>4:False y Not:True entonces mientras una condición de verdadero será True
#El Not es el contrario del resultado: si tenemos un True su contrario es False, si tenemos un False su contario es True.
#contrario de False es True, por eso es True el resultado.
#Not False es True y Not True es False
#El Not() niega toda la condición
