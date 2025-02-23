#STRINGS:

#LAS VARIABLES QUE SEAN DE TIPO STRING SE DEFINEN DE LA SIGUIENTE MANERA:
my_string = 'Mi String'
my_other_string = "Mi otro String" #Ejemplo del uso de ambas comillas

print(len(my_string)) #Medir la longitud 
print(len(my_other_string)) #No mide el nombre de la variable, mide la longitud del contenido de la variable

#1.-CONCATENACIÓN DE STRINGS
print(my_string + '' + my_other_string) #Se define una nueva cadena con los espacios dentro de las comillas

#LOS STRINGS PUEDEN LLEVAR CIERTOS CARACTERES:
my_new_line_string = 'Este es un String\ncon salto de línea' #\n sirve para salto de línea
print(my_new_line_string)

my_tab_line_string = '\tEste es un String con tabulación' #\t sirve para tabulación
print(my_tab_line_string)

my_scape_line_string = '\\tEste es un String\\ncon escapado' #\\ sirve para omitir/escaparse de lo impuesto
print(my_scape_line_string)

#COMO FORMATEAR DE ALGUNA FORMA LOS STRINGS:
#El formateo se utiliza cuando estamos internacionalizando texto.
#Ejemplo nuestro proyectos en inglés y español u otros idiomas, nos lo pone en el idioma que querramos.
name , surname , age = 'Carolina' , 'Bezares' , 24
#ESTA MANERA ES LA IDEAL AL TENER MUCHOS DATOS POR MEJOR MANEJO DE DATOS:
#Se utilizan las llaves cuando queremos que impriman tal cual el objeto:
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) #Esta es la manera para solamente strings
#Los porcentajes de %s, %d, %f es cuando en realidad estamos trabajando directamente con el número formateado
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) #Esta es la manera al mezclar string con int
#Lo que hace %s es: el primer texto que se pase formateado a la cadena de texto lo pone ahí.
#Lo que hace %d es: para formatear enteros.
#La forma ideal para es trabajar con los porcentajes porque es seguro que estamos imprimiendo tal cual la cadena de texto 
#o si necesitamos imprimir los números, al igual que es una manera segura para pasar el tipo de datos corrrecto.
#ESTA MANERA ES LA IDEAL AL TENER MUCHOS DATOS POR MEJOR MANEJO DE DATOS:

#1.1ESTA MANERA NO SE ACONSEJA HACER:
print('Mi nombre es' + name + '' + surname + 'y mi edad es' + str(age))#Al lenguaje le cuesta más ejecutar esto.
#Se aconsejan las dos anteriores y más si vas a formatear los datos.

#2.-INFERENCIA DE DATOS/INTERPOLACIÓN DE DATOS:
print(f'Mi nombre es {name} {surname} y mi edad es {age}')#La f ayuda a formatear y a inferir el valor de cada una de las variables.
#Si queremos imprimir los datos tal cual de una manera rapida, si queremos formatear los datos la mejor manera es definir el tipo de formato.

#3.-DESEMPAQUETADO DE CARACTERES: NO SE RECOMIENDA POR DIFICULTAD DE MANEJO DE DATOS AL TENER MUCHOS
lenguaje = 'Python' #Es una variable que la hemos llamado Python.-#Lenguaje tiene por valor cada una de las letras de la palabra de Python
#a-P, b-Y, c-T, d-H, e-O, f-N
a, b, c, d, e, f = lenguaje #Es una variable que la hemos igualado acá con cada una de las letras.
print(a)#De acuerdo a las letras que imprimas serán lo que se ejecute.
print(b)

#4.-DIVISIÓN:

lenguaje_slice = lenguaje[1:3] #Acá estamos pasando la variable que definimos anteriormente.
print(lenguaje_slice)
#Imprime la Y and T porque empieza a contar/posicionarse ignorando el primero y el tercero = 0-P, 1-Y, 2-T, 3-H, 4-O, 5-N

lenguaje_slice = lenguaje[1:]#Acá como no tenemos un final por lo tanto solo quita la primer posición
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]#Si empezamos por el final por eso nos da la letra 'O'
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2]#Acá hace los saltos para dar los datos que se piden.
print(lenguaje_slice)

#5.-REVERSA:DARLE LA VUELTA:
reversed_lenguaje = lenguaje[::-1]#Le está dando la vuelta a los datos de la variable y el final empieza desde el -1 porque como
#tal no hay un -0.
print(reversed_lenguaje)

#6.-FUNCIONES/MÉTODOS: DEL SISTEMA: 
#Ejemplo de algunas básicas
print(lenguaje.capitalize())#Si ponemos un punto después de la variable nos dará una lista de las operaciones disponibles para cadena de texto
#Lo que hace capitalize() es poner la primer letra en mayúscula aunque en la variable este definida con minúscula.
print(lenguaje.upper())#Pone todo en mayúscula
print(lenguaje.count('t'))#Lo que hará es contar el total de lo que se le indique y pondrá ese total, por ejemplo ahí es la 't'
print(lenguaje.isnumeric())#Acá nos indicará si es un número, dará como resultado False porque es un string 'Python'
#En este ejemplo añadiremos un True para ver su funcionalidad al identificar números
print('1'.isnumeric())#Da como resultado True
print(lenguaje.lower())#Para hacer todo en minúscula
print(lenguaje.upper().isupper())#Lo que hace isupper() es una comprobación de si está en mayúscula, por lo tanto dará True
print(lenguaje.lower().isupper())#Acá estamos indicando que el texto pase a minúscula por lo tanto comprobar si es mayúscula es False
print(lenguaje.startswith('Py'))#Es para comprobación del inicio y da un True o False-acá el ejemplo indicamos preguntando si empieza la variable 'Python' con 'py'
# que quiere decir si empieza con 'py' pero en minúscula o 'Py' con mayúscula.- Depende de la variable que ya definimos anteriormente
print('Py' == 'py') #Está haciendo un comparativo lo cual da un True o False como resultado.