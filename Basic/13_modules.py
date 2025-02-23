#MODULES -> Tipo acceder a las funciones de otras clases.
#Los modulos son una serie de operaciones y de utilidades que intente resolver problemas con alguna relación.

#Este ejemplo va con la clase 'module'.
#Modulos: Son como librerias en el que tenemos código.


#1.-ACCEDER A OTRO FICHERO CON LA PALABRA RESERVADA: import

import module #Estamos acciendo a la función de la clase.

module.sumValue(5, 3, 1) #Acceder a los datos que tiene la función entramos con 'module'. -> Ya podemos meter nuestros datos también. -> De esta manera tenemos que indicar la clase y la función.
module.printValue('Hola Python!')

from module import sumValue, printValue #Para importar un función en concreto de la clase es from seguido del nombre de la clase e import con el nombre de la función que queremos en concreto. -> Podemos importar más de una función a la vez.



sumValue(5, 3, 1) #Solo escribimo el nombre de la función ya que anteriormente con 'from' pedimos importar una función/operación en concreta.
printValue('Hola Python2')

#Modulos que definimos -> Los que están de la línea 20 hacía arriba.

#Modulos creados por el sistema -> Línea 24 en adelante.

import math

print(math.pi) #Este modulo ya no nos da unicamente una función, nos da el acceso a diferentes valores que pueden estar definidos por el sistema.
print(math.pow(2, 8))

#Importar y renombrar.
from math import pi as PI_VALUE #Estamos importando una función en especifico del modulo. -> También queremos darle un nombre muy concreto a la función o valor que estamos importando, le damos un alias: as


print(PI_VALUE) #Pasamos el alias