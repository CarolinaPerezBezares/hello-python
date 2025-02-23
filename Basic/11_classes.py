#CLASSES
#Son un objeto que nos sirve para definir una entidad. -> Una entidad acá es una persona 'MyEmptyPerson' y 'Person'.

#Pueden tener constructores. -> Una clase puede hacer cosas: Si tenemos uno de alguna manera sea capaz de recibir parametros.
#Todo lo que este dentro de la clase tiene que responder a cierta lógica.

#1.-DEFINIR UNA CLASE:Class
#Los nombres de las clases no van snake case va con camel case. -> Va en mayúscula cada primer letra sin espacios ni guiones bajos.

class MyEmptyPerson:
    pass #Evita el error para que ejecute. -> La clase va vacía

#Estanciar una clase: Podemos llamar a la clase de ambas maneras
print(MyEmptyPerson)
print(MyEmptyPerson()) #Los lleva cuando necesite algo para poder ejecutarse.

class Person(): #En el momento que pensamos en un objeto debe de tener parametros. -> Porque define
    def __init__(self, name, surname): #El init es reservado del sistema y nos sirve para crear un constructor de clase. -> Ya podemos recibir un parametro.
        self.name = name #Ya estamos almacenando los valores que le llegan. -> Si self ya tiene una propiedad que se llama 'name' y la igualamos a 'name' ya estamos asigando una propiedad.
        self.surname = surname #Si queremos crear una clase que tenga un constructor tiene que tener 'self'

my_person = Person('Carolina', 'Bezares') #Ya podemos asignar valores. -> Ya los puede recibir   -> Propiedad definida fuera.
print(f'{my_person.name} {my_person.surname}') #Ya que hemos creado a la persona ya podemos acceder a los valores.

class Person2():
    def __init__(self):  
        self.name = 'Carolina2' #Propiedad definida dentro
        self.surname = 'Bezares2'

my_person2 = Person2() #Ya no pasamos los nombres como parametro. -> Ya los definimos en el constructor.
print(f'{my_person2.name} {my_person2.surname}')

class Person3():
    def __init__(self, name, surname, alias = 'Sin alias'): #Por fuera no podemos acceder a nombre o apellido. -> Los valores.
        self.full_name = f'{name} {surname} ({alias})' #Ya no estamos almacenando los valores. -> Estamos creando una propiedad almacenada 'full_name'. -> Con los () solo indicamos que al mostrar el valor este dentro de ellos. -> Esto es una cadena de texto.
        self.__name = name #Con los 2 guines bajos '__' estamos volviendo la propiedad privada. -> La anterior es pública ya que podemos modificarle los valores después.

    def get_name (self): #Función para retornar el name y poder acceder para verlo. -> Solo podemos ver los valores no modificarlos.
        return self.__name

    def walk(self): #Añadir funciones. -> Una función dentro de una clase le podemos pasar pasar el parametro por defecto la cual es la forma de llamar a la misma clase y acceder a todo lo que este guardado ahí.
            print(f'{self.full_name} Esta caminando') #Dentro de nuestra clase podemos utilizar cuantas veces queramos a 'self'

my_person3 = Person3('Carolina3' , 'Bezares3') #Los valores son los que hemos calculado al momento de instanciar la clase.
print(my_person3.full_name) #Solo tenemos acceso a la propiedad 'full_name', que es la que hemos creado. -> Creamos una clase con una propiedad almacenada.
print(my_person3.get_name()) #Ya podemos acceder a verlos no a modificar. -> Se puede modificar creando un set.
my_person3.walk()

my_other_person = Person3('Carolina4', 'Bezares4', 'CarolinaBezares4') #Acá ya hemos dado un dato alias.
print(my_other_person.full_name)
my_other_person.walk() #Acá indicamos que camine.
my_other_person.full_name = 'Tsuki(La odisea de Tsuki)' #Estamos renombrando a los valores del parametro. -> Estamos dando un valor de cadena de texto.
print(my_other_person.full_name) #Podemos acceder a la clase, a las propiedades de ella, podemos cambiarla. -> Ya no con el constructor ya que es para crear la instancia/crear por primea vez ese objeto: Una vez creado podemos hacer lo que queramos con él.


    