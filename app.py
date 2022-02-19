# Este es un comentario de una sola linea
"""
este es un comentario de
multiples
lineas
"""

nombre = 'david' #string
cantidadMaterias = 3 #integer
numeroDecimal = 17.1 #float

diasSemana = ['lunes','martes','miercoles','jueves','viernes'] #listas o array
listaDinamica = [0, 'hola', 12.5, [0,1]]


print(diasSemana[2]) #mierocoles
print(listaDinamica[3][1]) #[0,1] #1

esMayorEdad = True #booleano

#diccionarios - JSON - Objets

persona = {
    'nombre': 'David',
    'apellido': 'Vivas',
    'edad': 23,
    'materias': ['base de datos 2', 'lengiaje 4g'],
} 

print(persona['nombre']) #david
print(persona['materias'][1])

#lista de diccionarios

personas = [
    {
        'nombre': 'David',
        'apellido': 'Vivas',
        'edad': 23,
        'materias': ['base de datos 2', 'lengiaje 4g'], 
    },
    {
        'nombre': 'Camilo',
        'apellido': 'Perez',
        'edad': 25,
        'materias': ['ingles', 'python'],
    },
    {
        'nombre': 'Carlos',
        'apellido': 'Sanchez',
        'edad': 22,
        'materias': ['base de datos 2', 'Lenguaje Orientado a Eventos'],
    }
]

print(personas[2]['materias'][1])

# condiciones
esMayorEdad = True
if esMayorEdad == True:
    print('Es mayor de edad')
    print('Esto es del if')
else:
    print('No es mayor de edad')
    print('Esto es parte del else')
    
print('Mensaje de prueba')

# ciclo para 

for per in personas:
    print(per['nombre'])
    
nombrePersona = 'roberto'
print(nombrePersona[2])  #imprime la b, toma roberto como un arreglo




#conjugacion de verbos
#len(variable) para medir cuantas letras hay
#variable.replace remmplaza algo en algo


#terminar de hacerlo
verbo = input('Ingrese verbo en infinitivo (ar-er-ir): \n')
"""
conjugacion = {
    'Yo':{
        'ar':'o',
        'er':'o',
        'ir':'o'
    },
    'Tú':{
        'ar':'as',
        'er':'es',
        'ir':'es'    
    },
    'Él':{
        'ar':'a',
        'er':'e',
        'ir':'e'    
    },
    'Nosotros':{
        'ar':'amos',
        'er':'emos',
        'ir':'imos'    
    }
}
"""


letraFin = verbo[len(verbo)-1] 
letraAnteFin = verbo [len(verbo)-2]
terminacion = letraAnteFin + letraFin 
verboSinTerminacion = verbo.replace(terminacion,'')

if terminacion == 'ar':
    print('Yo ',verboSinTerminacion+'o \n')
    print('Tú ',verboSinTerminacion+'as \n')
    print('Él ',verboSinTerminacion+'a \n')
    print('Ella ',verboSinTerminacion+'a \n')
    print('Nosotros ',verboSinTerminacion+'amos \n')
    print('Ellos ',verboSinTerminacion+'an \n')

if terminacion == 'er':
    print('Yo ',verboSinTerminacion+'o \n')
    print('Tú ',verboSinTerminacion+'es \n')
    print('Él ',verboSinTerminacion+'e \n')
    print('Ella ',verboSinTerminacion+'e \n')
    print('Nosotros ',verboSinTerminacion+'emos \n')
    print('Ellos ',verboSinTerminacion+'en \n')    

if terminacion == 'ir':
    print('Yo ',verboSinTerminacion+'o \n')
    print('Tú ',verboSinTerminacion+'es \n')
    print('Él ',verboSinTerminacion+'e \n')
    print('Ella ',verboSinTerminacion+'e \n')
    print('Nosotros ',verboSinTerminacion+'imos \n')
    print('Ellos ',verboSinTerminacion+'en \n')